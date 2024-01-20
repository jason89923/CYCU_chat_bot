import global_variable as gv
from pprint import pprint
import requests
import jwt
import time
import json
import timeit

APP_ID: str = gv.API.APP_ID
KEY : str = gv.API.KEY
LOGIN_URL :str = gv.API.Formal_LOGIN

URL: str = gv.API.Formal_URL
LB_INFO_MAP = {'館藏地': 'location', '索書號': 'id', '條碼': 'barcode', '狀態': 'status', '其他訊息': 'other'}


class API:
    @staticmethod
    def __get_formal_jwt():
        exp = time.time()
        exp = exp + 60
        encoded_jwt = jwt.encode(
            key=KEY,
            headers={
                "typ": "JWT",
                "alg": "HS512"
            },
            payload={
                "sub": APP_ID,
                "exp": exp
            }
        )
        return encoded_jwt
    @staticmethod
    def get_op_class(year, page=1):
        encoded_jwt = API.__get_formal_jwt()
        headers = {
            "Authorization": f'Bearer {encoded_jwt}',
            "User-Agent": 'Mozilla/5.0 (  NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            "enctype": "application/json"
        }
        url = URL + f"line/webhook/op_class/?YEAR_TERM={year}&page={page}"
        
        response = requests.post(url=url, headers=headers, timeout=8).json()
        return response

    @staticmethod
    def get_st_info(id):
        encoded_jwt = API.__get_formal_jwt()
        headers = {
            "Authorization": f'Bearer {encoded_jwt}',
            "User-Agent": 'Mozilla/5.0 (  NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            "enctype": "application/json"
        }
        url = URL + f"line/webhook/st_info/?IDCODE={id}"
        
        response = requests.post(url=url, headers=headers, timeout=5).json()
        return response

    @staticmethod
    def get_lb_info(opcode, year):
        primary_key = f'{opcode}-{year}'
        if gv.LB_INFO_CACHE.exists(primary_key):
            return json.loads(gv.LB_INFO_CACHE.get(primary_key))
        else:
            encoded_jwt = API.__get_formal_jwt()
            headers = {
                "Authorization": f'Bearer {encoded_jwt}',
                "User-Agent": 'Mozilla/5.0 (  NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                "enctype": "application/json"
            }
            url = URL + f"line/webhook/coursebook/?year={year}&opcode={opcode}"
            
            response = requests.post(url=url, headers=headers, timeout=20).json()
            def check_args(name, info_list, i):
                if name in i:
                    context = i[name].replace(' ', '').replace('\n', '').replace('\t', '')
                    if len(context) > 0:
                        info_list[name] = i[name]
            result = []
            if 'dataList' not in response:
                gv.LB_INFO_CACHE.set(primary_key, json.dumps(None), ex=3600)
                return None
            for i in response['dataList']:
                info_list = {}
                for name in ['title', 'edition', 'author', 'booktype']:
                    check_args(name, info_list, i)
                if 'webpac_info' in i:
                    for j in i['webpac_info'][0]:
                        if j['title'] in LB_INFO_MAP:
                            info_list[LB_INFO_MAP[j['title']]] = j['content']
                if info_list != {}:
                    result.append(info_list)
            if len(result) == 0:
                result = None
            gv.LB_INFO_CACHE.set(primary_key, json.dumps(result), ex=3600)
            return result

    @staticmethod
    def get_std_course_info(id: str,page=1):
        encoded_jwt = API.__get_formal_jwt()
        headers = {
            "Authorization": f'Bearer {encoded_jwt}',
            "User-Agent": 'Mozilla/5.0 (  NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            "enctype": "application/json"
        }
        url = URL + f"line/webhook/std_course/index.jsp?IDCODE={id}&PAGE={page}"
        
        response = requests.post(url=url, headers=headers, timeout=10).json()
        return response
    
    def itouch_login(uid):
        encoded_jwt = API.__get_formal_jwt()
        headers = {
            "Authorization": f'Bearer {encoded_jwt}',
            "User-Agent": 'Mozilla/5.0 (  NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            "enctype": "application/json"
        }
        # 測試階段 範圍: 目前在學、休學的學生，不下idcode即可查全部
        url = LOGIN_URL + f"/active_system/line/bind.jsp?line_uid={uid}&path=/home&isReturn=0"
        response = requests.post(url=url, headers=headers, timeout=5)
        return response.json()['link']
    
    @staticmethod
    def course_list(id_code):
        encoded_jwt = API.__get_formal_jwt()
        headers = {
            "Authorization": f'Bearer {encoded_jwt}',
            "User-Agent": 'Mozilla/5.0 (  NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            "enctype": "application/json"
        }
        url = URL + f"course/selected/?lang=tw&idcode={id_code}"
        
        response = requests.get(url=url, headers=headers, timeout=5).json()
        return response

    
    @staticmethod
    def get_std_id(uid):
        encoded_jwt = API.__get_formal_jwt()
        headers = {
            "Authorization": f'Bearer {encoded_jwt}',
            "User-Agent": 'Mozilla/5.0 (  NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            "enctype": "application/json"
        }
        # 測試階段 範圍: 目前在學、休學的學生，不下idcode即可查全部
        url = URL + f"line/users/?uid={uid}"
        
        response = requests.get(url=url, headers=headers, timeout=5)
        return response.json()['idcode']
    

    def del_acct(uid):
        encoded_jwt = API.__get_formal_jwt()
        headers = {
            "Authorization": f'Bearer {encoded_jwt}',
            "User-Agent": 'Mozilla/5.0 (  NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            "enctype": "application/json"
        }
        # 測試階段 範圍: 目前在學、休學的學生，不下idcode即可查全部
        url = URL + f"line/users/revoke/?uid={uid}"
        
        response = requests.post(url=url, headers=headers, timeout=5)
        return response.json()



def API_test():
    # pprint(API.get_op_class('1122'))

    # pprint(API.get_st_info('10944264'))  # 個人資訊 : 推薦
    # pprint(API.get_lb_info('GQ101V', '1112'))
    # pprint(API.get_std_course_info('10944264')) # 修課核對表 : 畢業門檻
    # pprint(API.itouch_login('Udb25939955755d2ea62f8accac1774e6'))
    # pprint(API.get_std_id('Udb25939955755d2ea62f8accac1774e6'))
    # pprint(API.add_idno('U824cac8fefdf7daf96bf16832667349d','G122476952'))
    # pprint(API.del_acct('U55e6eea5b53b07e974f06f8cf8b2f2f7'))
    pprint(API.course_list('10944264'))

if __name__ == '__main__':
    start_time = timeit.default_timer()
    
    course = API_test()
    
    end_time = timeit.default_timer()
    print('執行時間：', end_time - start_time)
    # reply_arr = []
    # for i in range(len(course['total']['this_year_st'][0]['st_score'])):
    #     try:
    #         if str(course['total']['this_year_st'][0]['st_score'][i]['cross_year_term'] or '?') == '1112':
    #             reply_arr.append((f"課程名稱 : {str(course['total']['this_year_st'][0]['st_score'][i]['curs_nm_c_s_a'])}\n課程代碼 : {str(course['total']['this_year_st'][0]['st_score'][i]['op_code_a'])}\n課程名稱 : {str(course['total']['this_year_st'][0]['st_score'][i]['curs_nm_c_s_a'])}\n---------------------\n"))
    #     except:
    #         print(str(course['total']['this_year_st'][0]['st_score'][0]))

    # print(reply_arr)
