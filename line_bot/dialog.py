import global_variable as gv
import json
import inspect
from formal_api import API 
from linebot.models import TextSendMessage, FlexSendMessage, StickerSendMessage
import re
import copy
from requests.exceptions import ReadTimeout
import random
import string
from Bubble import wb_message
import traceback
import std_course_info_mg
from datetime import datetime
from schedule.update_system_log import insert_line_error_message
import linebot.models as lineSDK





class User:

    def __init__(self, userID: str):
        self.userID = userID
        self.state: int = '主選單'
        """正在使用的功能, 初始為主選單"""
        self.current_input = None
        """最近一次的輸入內容"""
        self.waiting_for = None
        """正在等待的參數名稱, None表示不在等待狀態"""
        self.args: dict = {}
        """所需要的參數"""
        self.global_args: dict = {}
        """全域變數"""
        self.student_id = None
        self.student_dept = None
        self.abandoned = False
        self.year_term = None
        if gv.SESSION.exists(userID):
            value = gv.SESSION.get(userID)
            attrs = json.loads(value)
            for k, v in attrs.items():
                setattr(self, k, v)

    def clear(self):
        self.state: int = '主選單'
        self.waiting_for = None
        self.args: dict = {}

    def __repr__(self) -> str:
        return self.__dict__.__str__()

    def dump(self):
        if self.abandoned:
            gv.SESSION.delete(self.userID)
        else:
            gv.SESSION.set(self.userID, json.dumps(self.__dict__))

    @staticmethod
    def clear_all():
        gv.SESSION.flushdb()

    def clear_user_global_args(self, function_name):
        for parameter in self.global_args[function_name]:
            self.global_args[function_name][parameter] = []


class Sub_Function:
    def __init__(self, function_name: str):
        self.function_name = function_name


class Dialog_Manager:
    _developer_functions = set()
    _callback_map = {}
    _re_map = {}
    _QA_map = {}
    _global_args_map = {}
    current_user: User = None
    user_log = []
    isCommand = False
    
    @staticmethod
    def is_current_user_developer():
        return gv.g.current_user.userID in gv.DEVELOPER

    @staticmethod
    def __collect_parameters(user: User, message: str):
        if user.waiting_for is not None:
            user.args[user.waiting_for] = message

        for parameter in Dialog_Manager._callback_map[user.state]['parameters']:
            if parameter not in user.args:
                user.waiting_for = parameter
                return Dialog_Manager._callback_map[user.state]['parameters'][parameter]
        user.waiting_for = None
        return None

    @staticmethod
    def reply(userID: str, message: str):
        reply_array = []
        try:
            user = User(userID)
            gv.g.current_user = user
            user.current_input = message
            user.has_water_balloon = False
            Dialog_Manager.isCommand = False
            
            # 快速判斷是否登入，以及是否切換身分
            try:
                sid_from_api = API.quick_get_std_id(user.userID)
            except ReadTimeout:
                sid_from_api = user.student_id
            except:
                client = gv.mongo_client
                db = client.line_bot
                test_accoun_db = db['test_accoun_list']
                result = test_accoun_db.find_one({"line_id": user.userID})
                if result is None:
                    sid_from_api = None
                else:
                    sid_from_api = result['std_id']
                    
            if sid_from_api is None or user.student_id != sid_from_api:
                user.student_id = sid_from_api
                std_course_info = std_course_info_mg.insert_all_std_course_info(user.student_id)
                try:
                    user.student_dept = std_course_info['dep_name']
                except:
                    user.student_dept = None
                user.clear()
            
            
            # 紀錄系統日誌
            Dialog_Manager.user_log = [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), user.userID, str(user.student_id), user.current_input, str(user.state), str(user.waiting_for)]
            
            # 檢查未讀訊息 
            if user.student_id is not None and user.state == '主選單' and gv.WATER_BALLOONS_DATABASE.exists(user.student_id):
                reply_array.append([FlexSendMessage(alt_text="未讀訊息", contents=wb_message.wb_message_card(gv.WATER_BALLOONS_DATABASE.llen(user.student_id)))])
                user.has_water_balloon = True
            
            # 初始化全域變數
            if user.global_args == {}:
                user.global_args = copy.deepcopy(Dialog_Manager._global_args_map)
                
            # 基本問答判斷
            if message in Dialog_Manager._QA_map:
                Dialog_Manager.isCommand = True
                user.dump()
                return [[Dialog_Manager._QA_map[message]]]

            # 解碼使用者輸入
            for key, value in Dialog_Manager._re_map.items():
                if value.match(message):
                    message = key
                    break

            # 初始狀態
            if user.state == '主選單':
                isFunction = False
                if message in Dialog_Manager._callback_map:
                    isFunction = True
                    if message in Dialog_Manager._developer_functions and user.userID not in gv.DEVELOPER:
                        isFunction = False
                if isFunction:
                    user.state = message
                    Dialog_Manager.isCommand = True
                else:
                    reply_array.append([TextSendMessage(text='暫無此功能')])
                    return reply_array

            # 允許從參數收集階段跳回主選單
            if user.waiting_for is not None and (message in Dialog_Manager._callback_map or message == '主選單'):
                if not (message in Dialog_Manager._developer_functions and user.userID not in gv.DEVELOPER):
                    user.clear()
                    user.state = message
                    Dialog_Manager.isCommand = True
                    if user.state == '主選單':
                        user.dump()
                        return reply_array

            # 最後檢查是否登入，如果未登入，則切換狀態為登入
            if user.student_id is None and user.state != '登入' and message[:3] != '登入-':
                try:
                    user.student_id = API.get_std_id(user.userID)
                    std_course_info = std_course_info_mg.insert_all_std_course_info(user.student_id)
                    try:
                        user.student_dept = std_course_info['dep_name']
                    except:
                        user.student_dept = None
                except ReadTimeout:
                    raise e
                except:
                    user.state = '登入'

            # 執行參數收集
            return_msg = Dialog_Manager.__collect_parameters(user, message)
            if return_msg is not None:
                msg = []
                for i in return_msg:
                    if callable(i):
                        msg.append(i())
                    else:
                        msg.append(i)
                reply_array.append(msg)

            # 參數收集完畢，執行程式
            if user.state != '主選單' and user.waiting_for is None:
                try:
                    result = Dialog_Manager._callback_map[user.state]['function'](**user.args)
                    if result is None or result == []:
                        reply_array.append([TextSendMessage(text='暫無此功能')])
                    else:
                        reply_array.append(result)
                        
                    if user.waiting_for is None:
                        user.clear()
                except ReadTimeout as e:
                    raise e
                except Exception as e:
                    print(e)
                    user.clear()
                    reply_array.append([TextSendMessage(text="系統發生錯誤，已將錯誤回報給開發人員")])
                    reply_array.append([StickerSendMessage(package_id=6136, sticker_id=10551379)])
                    insert_line_error_message(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), user.userID, traceback.format_exc())
            
            # 檢查未讀訊息 
            if user.has_water_balloon:
                del reply_array[0]
            if user.student_id is not None and user.state == '主選單' and gv.WATER_BALLOONS_DATABASE.exists(user.student_id):
                reply_array.insert(0, [FlexSendMessage(alt_text="未讀訊息", contents=wb_message.wb_message_card(gv.WATER_BALLOONS_DATABASE.llen(user.student_id)))])
            user.dump()
        except ReadTimeout as e:
            reply_array.append([TextSendMessage(text='與校務系統的連結中斷，無法取得資料，請稍後再試')])
            return reply_array
        return reply_array

    @staticmethod
    def __get_parameter(name: str, default, parameter: dict):
        if name in parameter:
            return parameter[name]
        return default

    @staticmethod
    def bind(function_name: str, *args, **kwargs):
        """將function與對話綁定\n\nfunction_name: 要綁定的功能名稱, 會顯示於Line選單上\n\n*args: 要求使用者輸入對應參數時所傳送的文字 ex: '請輸入身高', '請輸入體重', ...\n\n**kwargs: 附加選項 ex: re=True"""

        def decorator(func, function_name: str, *args, **kwargs):
            param_list = list(inspect.signature(func).parameters)
            if len(param_list) < len(args):
                raise ValueError('參數設定錯誤')
            parameter_map = {}
            for i in range(len(args)):
                parameter_map[param_list[i]] = args[i]
            map = {'function': None, 'parameters': None}
            map['function'] = func
            map['parameters'] = parameter_map

            if Dialog_Manager.__get_parameter('re', False, kwargs):
                Dialog_Manager._re_map[function_name] = re.compile(function_name)
            if Dialog_Manager.__get_parameter('developer', False, kwargs):
                Dialog_Manager._developer_functions.add(function_name)
            Dialog_Manager._callback_map[function_name] = map

            return func
        return lambda func: decorator(func, function_name, *args, **kwargs)

    @staticmethod
    def set_global_args(function_name: str, parameter: str, value=[]):
        if function_name not in Dialog_Manager._global_args_map:
            Dialog_Manager._global_args_map[function_name] = {}
        Dialog_Manager._global_args_map[function_name][parameter] = value

    @staticmethod
    def create_test_acct_token(std_id: str):
        length_of_string = 8
        token = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
        gv.TEST_ACCOUNT_LOGIN_TOKEN.set(token, std_id, ex=60 * 15)
        return token

    @staticmethod
    def test_acct_login(line_id: str, token: str):
        if gv.TEST_ACCOUNT_LOGIN_TOKEN.exists(token):
            std_id = gv.TEST_ACCOUNT_LOGIN_TOKEN.get(token)
            gv.TEST_ACCOUNT_LOGIN_TOKEN.delete(token)
            client = gv.mongo_client
            db = client.line_bot
            test_accoun_db = db['test_accoun_list']
            test_accoun_db.insert_one({"line_id": line_id, "std_id": std_id, "token": token})
            return std_id

    @staticmethod
    def test_acct_signout(line_id: str):
        client = gv.mongo_client
        db = client.line_bot
        test_accoun_db = db['test_accoun_list']
        test_accoun_db.delete_one({"line_id": line_id})
        gv.g.current_user.abandoned = True
        
    @staticmethod
    def add_trigger(trigger_key: str, value: str):
        Dialog_Manager._QA_map[trigger_key] = value