import global_variable as gv
import os

from flask import Flask, request, abort, jsonify

import random
import json
import math
import json
from typing import Literal
from datetime import datetime
import pandas as pd
# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
import linebot.models as lineSDK
from Bubble import detail_basic, detail_ge, detail_ge_ex


from std_course_info_mg import insert_all_std_course_info
from hot_search import hot_search

from search_class import search_class


from schedule import update_system_log
from search_wishlist import wish_list
import delete_wishlist
from database import insert_wishlist
from formal_api import API
from Bubble import cls_type_selector, login_card, carousel, cls_schedule_selector, graduation_card, cond_result, library_result, cls_result, dept_card, feedback_card, next_page_card, suggest_cls_result, QA_card, school_opinion, system_opinion, wish_list_result, developer
import Bubble.water_balloons as wb
from apscheduler.schedulers.background import BackgroundScheduler
import glob
from dialog import Dialog_Manager
from get_time_condition import get_time_conditions
from cls_schedule import saveimage, hashlib_id
from miss_course import miss    # 這隻程式目前改寫，回傳較多資訊，function為 miss.temp_info，回傳資料形式 : [ 分數, 課程代碼, 學分數, 通過學年期 ]


'''
這是一個由中原大學資訊系及人工智慧學程老師與學生團隊開發的系統，由教務處學生學習發展中心管理，提供同學隨時掌握畢業門檻資訊，使您在選課及學習上不受阻礙。


本資料僅供學生選課參考，若有疑問請洽詢系所助理或教務處課註組各學系承辦人。
'''

line_bot_api = LineBotApi(gv.LINE_CHANNEL.ACCESS_TOKEN)
handler = WebhookHandler(gv.LINE_CHANNEL.SECRET)


app = Flask(__name__)


def delete_jpg_files():
    path = 'static/*.jpg'  # 替換成你的檔案路徑
    files = glob.glob(path)
    for f in files:
        os.remove(f)
        print(f"Deleted: {f}")

scheduler = BackgroundScheduler()
scheduler.add_job(func=delete_jpg_files, trigger='cron', hour=2)
scheduler.start()


delete_jpg_files()
'''
驗收時記得把1112都改成從API獲取
'''


@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    try:
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 驗證訊息來源
    except:
        return 'OK'                                           # 未通過驗證
    return 'OK'                                            # 通過驗證


@handler.add(lineSDK.MessageEvent, message=lineSDK.TextMessage)
def reply_text_message(event: lineSDK.MessageEvent):
    reply = []
    result = Dialog_Manager.reply(event.source.user_id, event.message.text)
    print(gv.g.current_user.userID)
    # 匯出使用者資訊
    Dialog_Manager.user_log.append(str(Dialog_Manager.isCommand))
    gv.USER_LOG.rpush('user_log', json.dumps(Dialog_Manager.user_log))

    for msg_list in result:
        for msg in msg_list:
            reply.append(msg)

    if len(reply) > 0:
        line_bot_api.reply_message(event.reply_token, reply)


# 貼圖
stickers = {
    446: [1988, 2027],
    789: [10855, 10894],
    1070: [17839, 17878],
    6136: [10551376, 10551399],
    6325: [10979904, 10979927],
    6359: [11069848, 11069871],
    6632: [11825374, 11825398],
    11538: [51626494, 51626533]
}


@handler.add(lineSDK.MessageEvent, message=lineSDK.StickerMessage)
def reply_sticker_message(event: lineSDK.MessageEvent):
    choice = random.choice(list(stickers.keys()))
    reply = lineSDK.StickerSendMessage(package_id=choice, sticker_id=random.choice(
        range(stickers[choice][0], stickers[choice][1] + 1)))
    line_bot_api.reply_message(event.reply_token, reply)


@handler.add(lineSDK.MessageEvent, message=lineSDK.ImageMessage)
def reply_image_message(event: lineSDK.MessageEvent):
    choice = random.choice(list(stickers.keys()))
    reply = lineSDK.StickerSendMessage(package_id=choice, sticker_id=random.choice(
        range(stickers[choice][0], stickers[choice][1] + 1)))
    line_bot_api.reply_message(event.reply_token, reply)


@handler.add(lineSDK.MessageEvent, message=lineSDK.LocationMessage)
def reply_image_message(event: lineSDK.MessageEvent):
    choice = random.choice(list(stickers.keys()))
    reply = lineSDK.StickerSendMessage(package_id=choice, sticker_id=random.choice(
        range(stickers[choice][0], stickers[choice][1] + 1)))
    line_bot_api.reply_message(event.reply_token, reply)


Dialog_Manager.set_global_args('查課', 'time')
Dialog_Manager.set_global_args('查課', 'teacher')
Dialog_Manager.set_global_args('查課', 'type')
Dialog_Manager.set_global_args('查課', 'name')
Dialog_Manager.set_global_args('查課', 'department')
Dialog_Manager.set_global_args('查課', 'page')

Dialog_Manager.set_global_args('推薦', 'type')
Dialog_Manager.set_global_args('推薦', 'page')

Dialog_Manager.set_global_args('追蹤', 'page')

Dialog_Manager.set_global_args('丟水球', 'std_id')
Dialog_Manager.set_global_args('丟水球', 'text')
Dialog_Manager.set_global_args('丟水球', 'curriculum')
Dialog_Manager.set_global_args('丟水球', 'subscription_list')

Dialog_Manager.set_global_args('詳細資訊', 'page')
Dialog_Manager.set_global_args('詳細資訊', 'data', None)

Dialog_Manager.set_global_args('系統改善', 'text')

cond_dict = {
    '上課時段': 'time',
    '課程類別': 'type',
    '授課老師': 'teacher',
    '課程名稱': 'name',
    '開課學系': 'department'
}


def page_bar(current_page: int, num_of_pages: int, function_name: str, width: int = 11):
    middle = math.floor(width / 2)
    start_index = current_page - middle if current_page - middle >= 1 else 1
    end_index = current_page + middle if current_page + middle <= num_of_pages else num_of_pages
    result = []
    if end_index == num_of_pages:
        for i in range(end_index, end_index - width, -1):
            if i <= 0:
                break
            result.insert(0, lineSDK.QuickReplyButton(action=lineSDK.MessageAction(label=i, text=f"{function_name}第{i}頁")))
    else:
        for i in range(start_index, start_index + width):
            if i > num_of_pages:
                break
            result.append(lineSDK.QuickReplyButton(action=lineSDK.MessageAction(label=i, text=f"{function_name}第{i}頁")))

    if current_page > 1:
        result.insert(0, lineSDK.QuickReplyButton(action=lineSDK.MessageAction(label='首頁', text=f'{function_name}首頁')))

    if current_page < num_of_pages:
        result.append(lineSDK.QuickReplyButton(action=lineSDK.MessageAction(label='末頁', text=f'{function_name}末頁')))

    return result


def search_course():
    reply_arr = []
    condition_map = gv.g.current_user.global_args['查課']
    gv.g.current_user.global_args['查課']['page'] = 1
    if condition_map['time'] == [] and condition_map['teacher'] == [] and condition_map['type'] == [] and condition_map['name'] == [] and condition_map['department'] == []:
        reply_arr.append(lineSDK.FlexSendMessage(alt_text='查詢條件', contents=cond_result.cond_result(gv.g.current_user.global_args['查課'])))
        return reply_arr
    result = search_class.batch_search(gv.CONFIG_CACHE.get('YEAR_TERM'), **gv.g.current_user.global_args['查課'])
    gv.SEARCH_COURSE_CACHE.set(gv.g.current_user.userID, json.dumps(result), ex=900)
    if result == []:
        reply_arr.append(lineSDK.FlexSendMessage(alt_text='查詢條件', contents=cond_result.cond_result(gv.g.current_user.global_args['查課'], 0, 0, 0)))
        return reply_arr
    cls_bubble = []
    num_of_result = len(result)
    total_page = math.ceil(num_of_result / gv.BUBBLE_MAX_PAGE)
    cls_bubble.append(cond_result.cond_result(gv.g.current_user.global_args['查課'], num_of_result, 1, total_page))
    for res in result[:gv.BUBBLE_MAX_PAGE]:
        cls_bubble.append(cls_result.cls_result_card(res))
    if (total_page > 1):
        cls_bubble.append(next_page_card.next_page_card('查詢課程'))
    hot_search.add_t_point(result[:gv.BUBBLE_MAX_PAGE])
    quick_reply_list = page_bar(1, total_page, '查詢課程')
    reply_arr.append(lineSDK.FlexSendMessage(alt_text="查課結果", contents=carousel.make_carousel(cls_bubble), quick_reply=lineSDK.QuickReply(items=quick_reply_list)))
    return reply_arr


def get_course(page=0, mode: Literal['absolute', 'offset'] = 'absolute'):
    reply_arr = []
    condition_map = gv.g.current_user.global_args['查課']
    if condition_map['time'] == [] and condition_map['teacher'] == [] and condition_map['type'] == [] and condition_map['name'] == [] and condition_map['department'] == []:
        reply_arr.append(lineSDK.FlexSendMessage(alt_text='查詢條件', contents=cond_result.cond_result(gv.g.current_user.global_args['查課'])))
        return reply_arr
    try:
        if mode == 'absolute':
            gv.g.current_user.global_args['查課']['page'] = page
        else:
            gv.g.current_user.global_args['查課']['page'] += page
        page = gv.g.current_user.global_args['查課']['page']
        if gv.SEARCH_COURSE_CACHE.exists(gv.g.current_user.userID):
            result = json.loads(gv.SEARCH_COURSE_CACHE.get(gv.g.current_user.userID))
        else:
            result = search_class.batch_search(gv.CONFIG_CACHE.get('YEAR_TERM'), **gv.g.current_user.global_args['查課'])
            gv.SEARCH_COURSE_CACHE.set(gv.g.current_user.userID, json.dumps(result), ex=900)
        if result == []:
            reply_arr.append(lineSDK.FlexSendMessage(alt_text='查詢條件', contents=cond_result.cond_result(gv.g.current_user.global_args['查課'], 0, 0, 0)))
            return reply_arr
        num_of_result = len(result)
        total_page = math.ceil(num_of_result / gv.BUBBLE_MAX_PAGE)
        if page > total_page:
            page = total_page
        elif page <= 0:
            page = 1
        gv.g.current_user.global_args['查課']['page'] = page
        result = result[(page - 1) * gv.BUBBLE_MAX_PAGE:page * gv.BUBBLE_MAX_PAGE]
        cls_bubble = []
        cls_bubble.append(cond_result.cond_result(gv.g.current_user.global_args['查課'], num_of_result, page, total_page))
        for res in result:
            cls_bubble.append(cls_result.cls_result_card(res))
        if page < total_page:
            cls_bubble.append(next_page_card.next_page_card('查詢課程'))
        hot_search.add_t_point(result)
        quick_reply_list = page_bar(page, total_page, '查詢課程')
        reply_arr.append(lineSDK.FlexSendMessage(alt_text="查課結果", contents=carousel.make_carousel(cls_bubble), quick_reply=lineSDK.QuickReply(items=quick_reply_list)))
    except:
        reply_arr.append(lineSDK.FlexSendMessage(alt_text='查詢條件', contents=cond_result.cond_result(gv.g.current_user.global_args['查課'])))
    return reply_arr


@Dialog_Manager.bind('查詢課程')
def search_course_time():
    return get_course(0, 'offset')


@Dialog_Manager.bind('^查詢課程(首|末)頁$', re=True)
def search_jump_page():
    msg = gv.g.current_user.current_input
    return get_course(1 if msg[4] == '首' else 99999, mode='absolute')


@Dialog_Manager.bind('^查詢課程第\d+頁$', re=True)
def search_which_page():
    msg = gv.g.current_user.current_input
    page = msg[5:-1]
    return get_course(int(page), mode='absolute')


@Dialog_Manager.bind('查詢課程下一頁')
def search_next_page():
    return get_course(1, mode='offset')


def check_args(arg, key):
    success = True
    if gv.g.current_user.global_args['查課']['page'] == []:
        gv.g.current_user.global_args['查課']['page'] = 1
    # 新增條件
    if arg not in gv.g.current_user.global_args['查課'][key]:
        gv.g.current_user.global_args['查課'][key].append(arg)
    else:
        success = False
    return success


def suggest(name, label, origin_label):
    result = hot_search.hot_course(gv.g.current_user.global_args['查課'], label)
    if len(result) == 0:
        return lineSDK.TextSendMessage(text="已無課程符合當前條件，請更改條件")
    quick_list = []
    course = []

    for i in result:
        if i[origin_label] not in course:
            quick_list.append(lineSDK.QuickReplyButton(action=lineSDK.MessageAction(label=i[origin_label], text=i[origin_label])))
        course.append(i[origin_label])
    return lineSDK.TextSendMessage(text=f"請輸入欲查詢{name}", quick_reply=lineSDK.QuickReply(items=quick_list))


@Dialog_Manager.bind('畢業門檻')
def graduation_threshold(student_id=None):
    if student_id is None:
        std_id = gv.g.current_user.student_id
    else:
        std_id = student_id
        
    if gv.g.current_user.student_dept is None or '碩' in gv.g.current_user.student_dept or '研究所' in gv.g.current_user.student_dept:
        return [lineSDK.TextSendMessage(text='十分抱歉!此功能僅供在校大學部使用!')]
    
    graduation_threshold = insert_all_std_course_info(std_id)
    reply_arr = []
    reply_arr.append(lineSDK.FlexSendMessage(
        alt_text="畢業門檻", contents=graduation_card.carousel(graduation_threshold)))
    return reply_arr


TF = {'A': 1, '1': 2, '2': 3, '3': 4, '4': 5, 'B': 6, '5': 7, '6': 8, '7': 9, '8': 10, 'C': 11, 'D': 12, 'E': 13, 'F': 14, 'G': 15}


def separate_date_time(name, location, date_time: str):
    result = []
    date_time_list = date_time.split('-')
    date = date_time_list[0]
    time_list = date_time_list[1]
    for time in time_list:
        result.append((int(date) + 1, TF[time], name, location))
    return result


def separate_multiple_date_time(name, location, date_time_list: list):
    result = []
    for date_time in date_time_list:
        if date_time is None:
            break
        result += separate_date_time(name, location, date_time)
    return result


@Dialog_Manager.bind('功課表')
def search_course_list(student_id=None):
    if student_id is None:
        std_id = gv.g.current_user.student_id
    else:
        std_id = student_id
    fileName = hashlib_id(std_id)
    reply_arr = []
    if (not gv.CURRICULUM_CACHE.exists(fileName)) or not os.path.exists(f'./static/{fileName}.jpg'):
        course = API.course_list(std_id)
        course_list = []
        result = []
        for i in range(len(course['dataList'])):
            course_list.append(course['dataList'][i]['op_code'])
            # name, location, date_time_list
            time_list = []
            time_1 = course['dataList'][i].get('op_time_1')
            if time_1:
                time_list.append(time_1)
            time_2 = course['dataList'][i].get('op_time_2')
            if time_2:
                time_list.append(time_2)
            time_3 = course['dataList'][i].get('op_time_3')
            if time_3:
                time_list.append(time_3)
            result += separate_multiple_date_time(course['dataList'][i]['curs_name'], course['dataList'][i]['cls_name'], time_list if time_list is not [] else '遠距教學')
        saveimage(std_id, gv.CONFIG_CACHE.get('SCHEDULE_YEAR_TERM'), result)
        gv.CURRICULUM_CACHE.set(fileName, fileName, ex=3600)
    reply_arr.append(lineSDK.ImageSendMessage(original_content_url=gv.URL + f'{fileName}.jpg', preview_image_url=gv.URL + f'{fileName}.jpg'))
    return reply_arr


@Dialog_Manager.bind('指定上課時段', [cls_schedule_selector.imagemap_message, lineSDK.TextSendMessage(text='請使用上方卡片點選欲搜尋時段，若無可透過鍵盤輸入如: 1-234 ')])
def search_course_time(time: str):
    conditions = get_time_conditions(time)
    if len(conditions) == 0:
        gv.g.current_user.waiting_for = 'time'
        reply_arr = []
        reply_arr.append(lineSDK.TextSendMessage(text='時間格式錯誤，請重新輸入'))
        reply_arr.append(cls_schedule_selector.imagemap_message)
        return reply_arr

    success_list = []
    reply_arr = []
    for condition in conditions:
        success_list.append(check_args(condition, 'time'))
    if True in success_list:
        reply_arr += search_course()
    else:
        reply_arr += get_course(0, mode='offset')
    return reply_arr


class_type = set(['天', '人', '物', '我', '宗哲', '人哲', '公民', '歷史', '體育', '英聽', '修辭', '延通', '軍訓', '系上課程', '教育學程'])


@Dialog_Manager.bind('指定課程類別', [cls_type_selector.imagemap_message, lineSDK.TextSendMessage(text='請使用上方卡片點選欲搜尋類別，若無可透過鍵盤輸入課程類別')])
def search_course_type(cls_type: str):
    cls_type = cls_type.replace(' ', '')
    if cls_type not in class_type:
        cls_type = '宗哲'
    reply_arr = []
    success = check_args(cls_type, 'type')
    if success:
        reply_arr += search_course()
    else:
        reply_arr += get_course(0, mode='offset')
    return reply_arr


@Dialog_Manager.bind('指定授課老師', [lambda: suggest('授課老師', 'teacher', 'teacher_cname')])
def search_course_teacher(teacher_name: str):
    teacher_name = teacher_name.replace(' ', '')
    reply_arr = []
    success = check_args(teacher_name, 'teacher')
    if success:
        reply_arr += search_course()
    else:
        reply_arr += get_course(0, mode='offset')
    return reply_arr


@Dialog_Manager.bind('指定課程名稱', [lambda: suggest('課程名稱', 'name', 'curs_nm_c_s')])
def search_course_name(cls_name: str):
    cls_name = cls_name.replace(' ', '')
    reply_arr = []
    success = check_args(cls_name, 'name')
    if success:
        reply_arr += search_course()
    else:
        reply_arr += get_course(0, mode='offset')
    return reply_arr


@Dialog_Manager.bind('指定開課學系', [lineSDK.FlexSendMessage(alt_text="開課學系", contents=dept_card.carousel()), lambda: suggest('開課學系', 'department', 'admin_dept_name')])
def search_course_department(dept_name: str):
    dept_name = dept_name.replace(' ', '')
    reply_arr = []
    success = check_args(dept_name, 'department')
    if success:
        reply_arr += search_course()
    else:
        reply_arr += get_course(0, mode='offset')
    return reply_arr


@Dialog_Manager.bind('清空所有條件')
def clear_all_condition():
    reply_arr = []
    gv.g.current_user.clear_user_global_args('查課')
    reply_arr.append(lineSDK.FlexSendMessage(alt_text='查詢條件', contents=cond_result.cond_result(gv.g.current_user.global_args['查課'])))
    return reply_arr


@Dialog_Manager.bind('^刪除(上課時段|課程類別|授課老師|課程名稱|開課學系)-\d+$', re=True)
def del_cond():
    msg = gv.g.current_user.current_input
    page = msg[7:]
    reply_arr = []
    if len(gv.g.current_user.global_args['查課'][cond_dict[msg[2:6]]]) != 0:
        del gv.g.current_user.global_args['查課'][cond_dict[msg[2:6]]][int(page) - 1]
        reply_arr += search_course()
    else:
        reply_arr += get_course(0, mode='offset')
    return reply_arr


@Dialog_Manager.bind('^清除(上課時段|課程類別|授課老師|課程名稱|開課學系)$', re=True)
def clear_cond():
    msg = gv.g.current_user.current_input
    reply_arr = []
    if len(gv.g.current_user.global_args['查課'][cond_dict[msg[2:]]]) != 0:
        gv.g.current_user.global_args['查課'][cond_dict[msg[2:]]] = []
        reply_arr += search_course()
    else:
        reply_arr += get_course(0, mode='offset')
    return reply_arr


feedback_stickers = [(11539, 52114110), (11539, 52114113),
                     (11537, 52002735), (6632, 11825393)]


def list_wish_list(page: int = 0, mode: str = 'absolute'):
    reply_arr = []
    if mode == 'offset':
        if gv.g.current_user.global_args['追蹤']['page'] == []:
            gv.g.current_user.global_args['追蹤']['page'] = 1
        gv.g.current_user.global_args['追蹤']['page'] += page
        page = gv.g.current_user.global_args['追蹤']['page']

    std_id = gv.g.current_user.student_id
    result = wish_list.search(std_id)
    num_of_result = len(result)
    if num_of_result == 0:
        reply_arr.append(lineSDK.TextSendMessage(text="當前追蹤清單為空，可以將查詢課程後喜歡的課程點選右上角的愛心加入至追蹤清單，也可以從追蹤清單點選右上角的愛心將此課程從追蹤清單移除。"))
        return reply_arr

    total_page = math.ceil(num_of_result / gv.BUBBLE_MAX_PAGE)
    if page > total_page:
        page = total_page
    elif page <= 0:
        page = 1

    result = result[gv.BUBBLE_MAX_PAGE * (page - 1):gv.BUBBLE_MAX_PAGE * page]
    cls_bubble = []
    for res in result:
        cls_bubble.append(wish_list_result.wish_list_result_card(res))
    if page < total_page:
        cls_bubble.append(next_page_card.next_page_card('追蹤清單'))
    quick_reply_list = page_bar(page, total_page, '追蹤清單')
    reply_arr.append(lineSDK.FlexSendMessage(alt_text="追蹤清單", contents=carousel.make_carousel(cls_bubble)))
    reply_arr.append(lineSDK.TextSendMessage(text=f'目前頁數: {page}/{total_page}', quick_reply=lineSDK.QuickReply(items=quick_reply_list)))
    gv.g.current_user.global_args['追蹤']['page'] = page
    return reply_arr


@Dialog_Manager.bind('追蹤清單')
def wishlist():
    return list_wish_list(0, 'offset')


@Dialog_Manager.bind('^追蹤清單第\d+頁$', re=True)
def suscribe_which_page():
    msg = gv.g.current_user.current_input
    page = int(msg[5:-1])

    return list_wish_list(page)


@Dialog_Manager.bind('追蹤清單下一頁')
def suscribe_next_page():
    return list_wish_list(1, mode='offset')


@Dialog_Manager.bind('^追蹤清單(首|末)頁$', re=True)
def suscribe_jump_page():
    msg = gv.g.current_user.current_input
    page = 1 if msg[4:-1] == '首' else 99999

    return list_wish_list(page)


@Dialog_Manager.bind('^將(\w*-\w*|\w*)加入追蹤清單$', re=True)
def suscribe_add():
    line_id = gv.g.current_user.userID
    msg = gv.g.current_user.current_input
    msg = msg[1:-6]
    if '-' in msg:
        splited = msg.partition('-')
    else:
        splited = ['XXXX', '-', msg]
    reply_arr = []
    if insert_wishlist.insert(splited[0], splited[2], gv.g.current_user.student_id, gv.CONFIG_CACHE.get('YEAR_TERM')):
        # if insert_wishlist.insert(splited[0], splited[2], line_id):
        reply_arr.append(lineSDK.TextSendMessage(text=f'已將{splited[2]}加入追蹤清單'))
        reply_arr += list_wish_list(99999)
    else:
        reply_arr.append(lineSDK.TextSendMessage(text=f'{splited[2]}已在追蹤清單內'))
        reply_arr += list_wish_list(0, mode='offset')
    return reply_arr


@Dialog_Manager.bind('^移除追蹤清單-\w*$', re=True)
def suscribe_remove():
    std_id = gv.g.current_user.student_id
    msg = gv.g.current_user.current_input
    op_code = msg[7:]
    reply_arr = []
    if delete_wishlist.delete_one(std_id, op_code):
        reply_arr.append(lineSDK.TextSendMessage(text=f'已從追蹤清移除{op_code}'))
    else:
        reply_arr.append(lineSDK.TextSendMessage(text=f'{op_code}不在追蹤清單內'))
    reply_arr += list_wish_list(0, mode='offset')
    return reply_arr


@Dialog_Manager.bind('^查詢\D\D\d\d\d\D之上課用書$', re=True)
def find_book():
    reply_arr = []
    msg = gv.g.current_user.current_input
    opcode = msg[2:8]
    info_list = API.get_lb_info(opcode, gv.CONFIG_CACHE.get('YEAR_TERM'))
    if info_list is None:
        return [lineSDK.TextSendMessage(text='本課程沒有上課用書')]

    num_of_page = math.ceil(len(info_list) / 10)
    for page in range(num_of_page):
        reply_arr.append(lineSDK.FlexSendMessage(alt_text="教科書查詢結果", contents=carousel.make_carousel([library_result.library_card(**i) for i in info_list[page * 10:(page + 1) * 10]])))
        if page >= 5:
            break
    return reply_arr




@Dialog_Manager.bind('結束話題')
def end_topic():
    gv.g.current_user.gpt_record.clear()
    return [lineSDK.TextSendMessage('好的，請問有甚麼我能幫助你的嗎?')]


@Dialog_Manager.bind('^功課表-\d+$', re=True, developer=True)
def search_course_list_developer():
    return search_course_list(gv.g.current_user.current_input[4:])


@Dialog_Manager.bind('^畢業門檻-\d+$', re=True, developer=True)
def graduation_threshold_developer():
    return graduation_threshold(gv.g.current_user.current_input[5:])


@Dialog_Manager.bind('^畢業門檻-\d+$', re=True, developer=True)
def graduation_threshold_developer():
    return graduation_threshold(gv.g.current_user.current_input[5:])


@Dialog_Manager.bind('測試帳號', [lineSDK.TextSendMessage(text='請輸入要綁定的學號')], developer=True)
def generate_test_acct_token(std_id: str):
    token = Dialog_Manager.create_test_acct_token(std_id)
    return [lineSDK.TextSendMessage(text='15分鐘內有效，僅限使用一次'), lineSDK.TextSendMessage(text=token)]


def login_message():
    message = []
    try:
        if gv.g.current_user.student_id is None:
            message.append(lineSDK.FlexSendMessage(alt_text='登入', contents=(login_card.login_bubble(gv.g.current_user.userID))))
            message.append(lineSDK.TextSendMessage(text='偵測到未登入，請點選當前最新的登入按鈕進入itouch進行登入，若按鈕失效請重新輸入「登入」，並點選最新的登入按鈕進行登入'))
        else:
            message.append(lineSDK.TextSendMessage(text=f'已登入成功，學號: {gv.g.current_user.student_id}'))
    except:
        message.append(lineSDK.TextSendMessage(text=f'訪問過快，請稍後再試'))
    return message


@Dialog_Manager.bind('登入')
def login():
    return login_message()


@Dialog_Manager.bind('登入-.+$', re=True)
def login():
    reply_arr = []
    if gv.g.current_user.student_id is not None:
        gv.g.current_user.clear()
        return [lineSDK.TextSendMessage(text=f'已完成登入，學號: {gv.g.current_user.student_id}')]

    input_token = gv.g.current_user.current_input[3:]
    if input_token == 'demo':
        token = Dialog_Manager.create_test_acct_token('10927147')
        std_id = Dialog_Manager.test_acct_login(gv.g.current_user.userID, token)
        reply_arr.append(lineSDK.TextSendMessage(text=f'已註冊為展示帳號'))
        return reply_arr
    std_id = Dialog_Manager.test_acct_login(gv.g.current_user.userID, input_token)
    if std_id is not None:
        reply_arr.append(lineSDK.TextSendMessage(text=f'已註冊為測試帳號，綁定學號: {std_id}'))
        return reply_arr


@Dialog_Manager.bind('登出', developer=True)
def signout():
    Dialog_Manager.test_acct_signout(gv.g.current_user.userID)
    API.del_acct(gv.g.current_user.userID)
    gv.g.current_user.abandoned = True
    return [lineSDK.TextSendMessage('已登出')]


def miss_course(result, page=1):
    if gv.g.current_user.student_dept is None or '碩' in gv.g.current_user.student_dept or '研究所' in gv.g.current_user.student_dept:
        return [lineSDK.TextSendMessage(text='十分抱歉!此功能僅供在校大學部使用!')]
    reply_arr = []
    if len(result) > 0:
        num_of_result = len(result)
        total_page = math.ceil(num_of_result / gv.BUBBLE_MAX_PAGE)
        cls_bubble = []
        for res in result[gv.BUBBLE_MAX_PAGE * (page - 1):gv.BUBBLE_MAX_PAGE * page]:
            if res == []:
                return [lineSDK.TextSendMessage(text='無推薦課程，錯誤訊息:此筆資料為空list')]
            cls_bubble.append(suggest_cls_result.suggest_cls_result_card(res))
        if page < total_page:
            cls_bubble.append(next_page_card.next_page_card('推薦課程'))
        quick_reply_list = page_bar(page, total_page, '推薦課程')
        reply_arr.append(lineSDK.FlexSendMessage(alt_text="推薦課程清單", contents=carousel.make_carousel(cls_bubble)))
        reply_arr.append(lineSDK.TextSendMessage(text=f'目前頁數: {page}/{total_page}', quick_reply=lineSDK.QuickReply(items=quick_reply_list)))
    else:
        reply_arr.append(lineSDK.TextSendMessage(text='該領域已修習完畢或本學期無開設該領域課程供修習，若無推薦課程可點選畢業門檻之詳細資料參閱當前修課情形，此功能僅供參考，正確資訊請參閱校方網站。'))
    
    return reply_arr


def set_recommend_course(function_name: str):
    if gv.g.current_user.student_dept is None or '碩' in gv.g.current_user.student_dept or '研究所' in gv.g.current_user.student_dept:
        return [lineSDK.TextSendMessage(text='十分抱歉!此功能僅供在校大學部使用!')]
    result, text = miss.recommend(gv.g.current_user.student_id, gv.g.current_user.student_dept, function_name, gv.CONFIG_CACHE.get('YEAR_TERM'))
    gv.RECOMMEND_COURSE_CACHE.set(gv.g.current_user.userID, json.dumps(result), ex=900)
    gv.g.current_user.global_args['推薦']['page'] = 1
    return miss_course(result)


def get_recommend_course(page, mode='absolute'):
    if gv.g.current_user.student_dept is None or '碩' in gv.g.current_user.student_dept or '研究所' in gv.g.current_user.student_dept:
        return [lineSDK.TextSendMessage(text='十分抱歉!此功能僅供在校大學部使用!')]
    if gv.g.current_user.global_args['推薦']['type'] == []:
        return graduation_threshold()
    if mode == 'absolute':
        gv.g.current_user.global_args['推薦']['page'] = page
    else:
        gv.g.current_user.global_args['推薦']['page'] += page
    page = gv.g.current_user.global_args['推薦']['page']
    if gv.RECOMMEND_COURSE_CACHE.exists(gv.g.current_user.userID):
        result = json.loads(gv.RECOMMEND_COURSE_CACHE.get(gv.g.current_user.userID))
    else:
        result, text = miss.recommend(gv.g.current_user.student_id, gv.g.current_user.student_dept, gv.g.current_user.global_args['推薦']['type'], gv.CONFIG_CACHE.get('YEAR_TERM'))
        gv.RECOMMEND_COURSE_CACHE.set(gv.g.current_user.userID, json.dumps(result), ex=900)
    num_of_result = len(result)
    total_page = math.ceil(num_of_result / gv.BUBBLE_MAX_PAGE)
    if page > total_page:
        page = total_page
    elif page <= 0:
        page = 1
    gv.g.current_user.global_args['推薦']['page'] = page
    return miss_course(result, page)


@Dialog_Manager.bind('^推薦(基本知能|基礎必修通識|學系必修|學系選修|延伸選修通識)課程$', re=True)
def recommend_course():
    insert_all_std_course_info(gv.g.current_user.student_id)
    function_name = gv.g.current_user.current_input[2:-2]
    user_log = gv.g.current_user.global_args['推薦']
    if user_log['page'] == []:
        user_log['page'] = 1
        user_log['type'] = function_name
        return set_recommend_course(function_name)
    if function_name == user_log['type']:
        return get_recommend_course(0, 'offset')
    else:
        user_log['page'] = 1
        user_log['type'] = function_name
        return set_recommend_course(function_name)


@Dialog_Manager.bind('推薦課程下一頁')
def recommend_next_page():
    insert_all_std_course_info(gv.g.current_user.student_id)
    return get_recommend_course(1, mode='offset')


@Dialog_Manager.bind('^推薦課程(首|末)頁$', re=True)
def recommend_jump_page():
    insert_all_std_course_info(gv.g.current_user.student_id)
    msg = gv.g.current_user.current_input
    page = 1 if msg[4:-1] == '首' else 99999
    return get_recommend_course(page)


@Dialog_Manager.bind('^推薦課程第\d+頁$', re=True)
def recommend_which_page():
    insert_all_std_course_info(gv.g.current_user.student_id)
    msg = gv.g.current_user.current_input
    page = msg[5:-1]
    return get_recommend_course(int(page), mode='absolute')


@Dialog_Manager.bind('意見回饋')
def feedback():
    return [lineSDK.FlexSendMessage(alt_text="意見回饋", contents=feedback_card.feedback_card())]


@Dialog_Manager.bind('校方回饋')
def common_problem():
    return [lineSDK.FlexSendMessage(alt_text="校方回饋", contents=school_opinion.carousel())]


@Dialog_Manager.bind('表單')
def common_problem():
    return [lineSDK.StickerSendMessage(6136, 10551377)]


def common_problem_card():
    message = gv.g.current_user.global_args['系統改善']['text']
    return [lineSDK.FlexSendMessage(alt_text="系統改善", contents=system_opinion.system_opinion_card(message))]


@Dialog_Manager.bind('系統改善')
def common_problem():
    return common_problem_card()


@Dialog_Manager.bind('系統改善-建議', [lineSDK.TextSendMessage(text='請輸入建議')])
def common_problem(message: str):
    gv.g.current_user.global_args['系統改善']['text'] = message
    return common_problem_card()


@Dialog_Manager.bind('系統改善-送出')
def common_problem():
    if gv.g.current_user.global_args['系統改善']['text'] == []:
        return common_problem_card()
    update_system_log.insert_system_feedback(gv.g.current_user.userID, gv.g.current_user.student_id, gv.g.current_user.global_args['系統改善']['text'])
    return [lineSDK.TextSendMessage(text='感謝你的建議!')]


@Dialog_Manager.bind('僅供參考')
def reference():
    return [lineSDK.TextSendMessage('本資料僅供學生選課參考，若有疑問請洽詢系所助理或教務處課註組各學系承辦人。')]


@Dialog_Manager.bind('謹言慎行')
def reference():
    return [lineSDK.TextSendMessage('溫馨提醒：請以尊重、友善、包容的語氣傳送每一則水球，勿傳送冒犯或不適當的訊息。請注意，我們的系統會記錄所有使用者的使用軌跡，違規的行為將可能導致此功能被禁用，情節重大者以校規論處，謝謝您的理解與配合。')]


def Q_and_A_excel():
    df = pd.read_excel('/home/tliw1/Cycu_line_bot/line_bot/Q&A.xlsx')
    type_question_map = {}
    for index, row in df.iterrows():
        msg_type = row['分類'].replace('_x000d_', '\n')
        question = row['問題'].replace('_x000d_', '\n')
        answer = row['答案'].replace('_x000d_', '\n')
        link = row['連結'].replace('_x000d_', '\n') if type(row['連結']) is str else None
        Dialog_Manager.add_trigger(question, lineSDK.FlexSendMessage(alt_text=answer[:10], contents=QA_card.make_answer_card(msg_type, answer, link)))
        if msg_type not in type_question_map:
            type_question_map[msg_type] = []
        type_question_map[msg_type].append(QA_card.make_question_card(msg_type, question))

    for key, value in type_question_map.items():
        Dialog_Manager.add_trigger(key, lineSDK.FlexSendMessage(alt_text=key[:10], contents=carousel.make_carousel(value)))
    Dialog_Manager.add_trigger('常見問題', lineSDK.FlexSendMessage(alt_text="常見問題", contents=carousel.make_carousel([QA_card.make_type_card(i) for i in type_question_map.keys()])))


def water_balloons_list():
    return [lineSDK.FlexSendMessage(alt_text="丟水球", contents=wb.water_polo_card(**gv.g.current_user.global_args['丟水球']))]


@Dialog_Manager.bind('丟水球')
def water_balloons():
    return water_balloons_list()


@Dialog_Manager.bind('丟水球-學號', [lineSDK.TextSendMessage(text='請輸入學號')])
def water_balloons(std_id: str):
    std_id = ''.join([c for c in std_id if c.isdigit()])
    if len(std_id) == 0:
        return water_balloons_list()
    gv.g.current_user.global_args['丟水球']['std_id'] = std_id
    return water_balloons_list()


@Dialog_Manager.bind('丟水球-訊息', [lineSDK.TextSendMessage(text='請輸入訊息')])
def water_balloons(message: str):
    gv.g.current_user.global_args['丟水球']['text'] = message
    return water_balloons_list()


@Dialog_Manager.bind('丟水球-清除訊息')
def water_balloons():
    gv.g.current_user.global_args['丟水球']['text'] = []
    return water_balloons_list()


@Dialog_Manager.bind('丟水球-功課表')
def water_balloons():
    if gv.g.current_user.global_args['丟水球']['curriculum'] == []:
        gv.g.current_user.global_args['丟水球']['curriculum'] = gv.g.current_user.student_id
    else:
        gv.g.current_user.global_args['丟水球']['curriculum'] = []
    return water_balloons_list()


@Dialog_Manager.bind('丟水球-追蹤清單')
def water_balloons():
    if gv.g.current_user.global_args['丟水球']['subscription_list'] == []:
        gv.g.current_user.global_args['丟水球']['subscription_list'] = gv.g.current_user.student_id
    else:
        gv.g.current_user.global_args['丟水球']['subscription_list'] = []
    return water_balloons_list()


@Dialog_Manager.bind('丟水球-送出')
def water_balloons():
    std_id = gv.g.current_user.global_args['丟水球']['std_id']
    if std_id == []:
        return [lineSDK.TextMessage(text=f'請輸入目標學號')]
    gv.WATER_BALLOONS_DATABASE.rpush(std_id, json.dumps({'source_id': gv.g.current_user.student_id, 'message': gv.g.current_user.global_args['丟水球']}))
    return [lineSDK.TextMessage(text=f'已送出訊息給{std_id}')]

@Dialog_Manager.bind('開發者回覆', [lineSDK.TextSendMessage(text='請輸入學號')], [lineSDK.TextSendMessage(text='請輸入訊息')], developer=True)
def developer_water_balloons(std_id: str, message: str):
    std_id = std_id.replace(' ', '')
    gv.WATER_BALLOONS_DATABASE.lpush(std_id, json.dumps({'source_id': "開發團隊", 'message': {"text": message, "curriculum": [], "subscription_list": []}}))
    return [lineSDK.TextMessage(text=f'已送出訊息給{std_id}')]

def send_any_message(identity: str, target_id: str, message: str):
    if not gv.WATER_BALLOONS_DATABASE.exists(gv.g.current_user.student_id):
        gv.WATER_BALLOONS_DATABASE.lpush(target_id, json.dumps({'source_id': identity, 'message': {"text": message, "curriculum": [], "subscription_list": []}}))

@Dialog_Manager.bind('水球追蹤清單下一頁')
def list_wish_list_for_balloons():
    reply_arr = []
    try:
        page = gv.g.current_user.shared_page

        std_id = gv.g.current_user.shared_std_id
        result = wish_list.search(std_id)
        num_of_result = len(result)
        if num_of_result == 0:
            reply_arr.append(lineSDK.TextSendMessage(text=f"{std_id}的追蹤清單為空。"))
            del gv.g.current_user.shared_page
            return reply_arr

        total_page = math.ceil(num_of_result / gv.BUBBLE_MAX_PAGE)
        result = result[gv.BUBBLE_MAX_PAGE * (page - 1):gv.BUBBLE_MAX_PAGE * page]
        cls_bubble = []
        for res in result:
            cls_bubble.append(cls_result.cls_result_card(res))
        if page < total_page:
            cls_bubble.append(next_page_card.next_page_card('水球追蹤清單'))
        reply_arr.append(lineSDK.FlexSendMessage(alt_text="水球追蹤清單", contents=carousel.make_carousel(cls_bubble)))
        gv.g.current_user.shared_page += 1
        if gv.g.current_user.shared_page > total_page:
            del gv.g.current_user.shared_page
            del gv.g.current_user.shared_std_id

        if gv.WATER_BALLOONS_DATABASE.llen(gv.g.current_user.student_id) > 0:
            quick_reply = lineSDK.QuickReplyButton(action=lineSDK.MessageAction(label='下一則訊息', text='查看未讀訊息'))
            reply_arr[-1].quick_reply = lineSDK.QuickReply(items=[quick_reply])
    except:
        gv.g.current_user.clear()
    return reply_arr


@Dialog_Manager.bind('查看未讀訊息')
def check_WB():
    reply = []
    if gv.WATER_BALLOONS_DATABASE.exists(gv.g.current_user.student_id):
        message_package = json.loads(gv.WATER_BALLOONS_DATABASE.lpop(gv.g.current_user.student_id))
        source_id = message_package['source_id']
        message = message_package['message']
        reply.append(lineSDK.TextSendMessage(text=f'來自 {source_id}'))
        if message['text'] != []:
            reply.append(lineSDK.TextSendMessage(text=message['text']))
        if message['curriculum'] != []:
            reply += search_course_list(source_id)
        if message['subscription_list'] != []:
            gv.g.current_user.shared_std_id = source_id
            gv.g.current_user.shared_page = 1
            reply += list_wish_list_for_balloons()

    else:
        reply.append(lineSDK.TextSendMessage(text='你目前沒有未讀訊息哦'))
    if gv.WATER_BALLOONS_DATABASE.llen(gv.g.current_user.student_id) > 0:
        quick_reply = lineSDK.QuickReplyButton(action=lineSDK.MessageAction(label='下一則訊息', text='查看未讀訊息'))
        reply[-1].quick_reply = lineSDK.QuickReply(items=[quick_reply])
    return reply


def course_detail(page: int = 0, mode: str = 'absolute'):
    reply_arr = []
    if gv.g.current_user.student_dept is None or '碩' in gv.g.current_user.student_dept or '研究所' in gv.g.current_user.student_dept:
        return [lineSDK.TextSendMessage(text='十分抱歉!此功能僅供在校大學部使用!')]
    
    if mode == 'offset':
        if gv.g.current_user.global_args['詳細資訊']['page'] == []:
            gv.g.current_user.global_args['詳細資訊']['page'] = 1
        gv.g.current_user.global_args['詳細資訊']['page'] += page
        page = gv.g.current_user.global_args['詳細資訊']['page']

    if gv.g.current_user.global_args['詳細資訊']['data'] is None:
        result = miss.temp_info(gv.g.current_user.student_id)
        gv.g.current_user.global_args['詳細資訊']['data'] = expand_dictionary(result, '學系必修')
    result = gv.g.current_user.global_args['詳細資訊']['data']
    num_of_result = len(result)

    total_page = math.ceil(num_of_result / gv.BUBBLE_MAX_PAGE)
    if page > total_page:
        page = total_page
    elif page <= 0:
        page = 1

    if num_of_result == 0:
        reply_arr.append(lineSDK.TextSendMessage(text="你目前仍未修習該分項中的任何課程。"))
        gv.g.current_user.global_args['詳細資訊']['page'] = page
        return reply_arr

    result = result[gv.BUBBLE_MAX_PAGE * (page - 1):gv.BUBBLE_MAX_PAGE * page]
    detail_bubble = []
    for res in result:
        if res[-1] == 1:
            if res[-2] == 'False':
                detail_bubble.append(detail_basic.fail_card(*res[:-2]))
            else:
                detail_bubble.append(detail_basic.pass_card(*res[:-1]))
        elif res[-1] == 2:
            if res[-2] == 'False':
                detail_bubble.append(detail_ge.fail_card(*res[:-2]))
            else:
                detail_bubble.append(detail_ge.pass_card(*res[:-1]))
        elif res[-1] == 3:
            if res[-2] == 'False':
                detail_bubble.append(detail_ge_ex.fail_card(*res[:-2]))
            else:
                detail_bubble.append(detail_ge_ex.pass_card(*res[:-1]))
    if page < total_page:
        detail_bubble.append(next_page_card.next_page_card_detail('詳細資訊'))
    quick_reply_list = page_bar(page, total_page, '詳細資訊')
    reply_arr.append(lineSDK.FlexSendMessage(alt_text="詳細資訊", contents=carousel.make_carousel(detail_bubble)))
    reply_arr.append(lineSDK.TextSendMessage(text=f'目前頁數: {page}/{total_page}', quick_reply=lineSDK.QuickReply(items=quick_reply_list)))
    gv.g.current_user.global_args['詳細資訊']['page'] = page
    return reply_arr


@Dialog_Manager.bind('^詳細資訊第\d+頁$', re=True)
def course_detail_which_page():
    insert_all_std_course_info(gv.g.current_user.student_id)
    msg = gv.g.current_user.current_input
    page = int(msg[5:-1])
    return course_detail(page)


@Dialog_Manager.bind('詳細資訊下一頁')
def course_detail_next_page():
    insert_all_std_course_info(gv.g.current_user.student_id)
    return course_detail(1, mode='offset')


@Dialog_Manager.bind('^詳細資訊(首|末)頁$', re=True)
def course_detail_jump_page():
    insert_all_std_course_info(gv.g.current_user.student_id)
    msg = gv.g.current_user.current_input
    page = 1 if msg[4:-1] == '首' else 99999

    return course_detail(page)


def expand_dictionary(dictionary: dict, specify_type=None, level=1):
    result = []
    if specify_type is None:
        for key, value in dictionary.items():
            if type(value) is dict:
                for i in expand_dictionary(value, level=level + 1):
                    result.append((key, *i))
            else:
                result.append((key, *[str(i) for i in value], level))
    else:
        dictionary = dictionary[specify_type]
        for key, value in dictionary.items():
            if type(value) is dict:
                for i in expand_dictionary(value, level=level + 1):
                    result.append((specify_type, key, *i))
            else:
                result.append((specify_type, key, *[str(i) for i in value], level))
    return result


@Dialog_Manager.bind('基本知能詳細資訊')
def dept_must_detail():
    insert_all_std_course_info(gv.g.current_user.student_id)
    if gv.g.current_user.student_dept is None or '碩' in gv.g.current_user.student_dept or '研究所' in gv.g.current_user.student_dept:
        return [lineSDK.TextSendMessage(text='十分抱歉!此功能僅供在校大學部使用!')]
    result = miss.temp_info(gv.g.current_user.student_id)
    gv.g.current_user.global_args['詳細資訊']['data'] = expand_dictionary(result, '基本知能')
    return course_detail()


@Dialog_Manager.bind('基礎必修通識詳細資訊')
def dept_must_detail():
    insert_all_std_course_info(gv.g.current_user.student_id)
    if gv.g.current_user.student_dept is None or '碩' in gv.g.current_user.student_dept or '研究所' in gv.g.current_user.student_dept:
        return [lineSDK.TextSendMessage(text='十分抱歉!此功能僅供在校大學部使用!')]
    result = miss.temp_info(gv.g.current_user.student_id)
    gv.g.current_user.global_args['詳細資訊']['data'] = expand_dictionary(result, '基礎必修通識')
    return course_detail()


@Dialog_Manager.bind('學系必修詳細資訊')
def dept_must_detail():
    insert_all_std_course_info(gv.g.current_user.student_id)
    if gv.g.current_user.student_dept is None or '碩' in gv.g.current_user.student_dept or '研究所' in gv.g.current_user.student_dept:
        return [lineSDK.TextSendMessage(text='十分抱歉!此功能僅供在校大學部使用!')]
    result = miss.temp_info(gv.g.current_user.student_id)
    gv.g.current_user.global_args['詳細資訊']['data'] = expand_dictionary(result, '學系必修')
    return course_detail()


@Dialog_Manager.bind('學系選修詳細資訊')
def dept_must_detail():
    insert_all_std_course_info(gv.g.current_user.student_id)
    if gv.g.current_user.student_dept is None or '碩' in gv.g.current_user.student_dept or '研究所' in gv.g.current_user.student_dept:
        return [lineSDK.TextSendMessage(text='十分抱歉!此功能僅供在校大學部使用!')]
    result = miss.temp_info(gv.g.current_user.student_id)
    gv.g.current_user.global_args['詳細資訊']['data'] = expand_dictionary(result, '學系選修')
    return course_detail()


@Dialog_Manager.bind('延伸選修通識詳細資訊')
def dept_must_detail():
    insert_all_std_course_info(gv.g.current_user.student_id)
    if gv.g.current_user.student_dept is None or '碩' in gv.g.current_user.student_dept or '研究所' in gv.g.current_user.student_dept:
        return [lineSDK.TextSendMessage(text='十分抱歉!此功能僅供在校大學部使用!')]
    result = miss.temp_info(gv.g.current_user.student_id)
    gv.g.current_user.global_args['詳細資訊']['data'] = expand_dictionary(result, '延伸選修通識')
    return course_detail()


@Dialog_Manager.bind('其他修課紀錄')
def dept_must_detail():
    insert_all_std_course_info(gv.g.current_user.student_id)
    if gv.g.current_user.student_dept is None or '碩' in gv.g.current_user.student_dept or '研究所' in gv.g.current_user.student_dept:
        return [lineSDK.TextSendMessage(text='十分抱歉!此功能僅供在校大學部使用!')]
    result = miss.temp_info(gv.g.current_user.student_id)
    gv.g.current_user.global_args['詳細資訊']['data'] = expand_dictionary(result, '其他選修') + expand_dictionary(result, '自由選修')
    return course_detail()


@Dialog_Manager.bind('亮')
def easter_egg():
    send_any_message('開發者-何亮頡', gv.g.current_user.student_id, '每一顆心都有最嚮往的地方，要堅持就會聽見奇蹟的聲響\nhttps://youtu.be/HI4P3Z8yiUY')
    return [lineSDK.FlexSendMessage(alt_text="開發者-何亮頡", contents=developer.liang())]


@Dialog_Manager.bind('gu')
def easter_egg():
    send_any_message('開發者-江晨銘', gv.g.current_user.student_id, '這是最後的一刻，誰都要學的一課 https://www.youtube.com/watch?v=eZh1mC1vPgw')
    return [lineSDK.FlexSendMessage(alt_text="開發者-江晨銘", contents=developer.gu())]


@Dialog_Manager.bind('zhe')
def easter_egg():
    send_any_message(random.choice(['即將消逝的學程"A̷̭̬͕̳̜̝͇͍̪͚̖͎͚͙̩̘̮̟̦͙̟̟͇̣̍̓͐̋̍̃́̍̊̑̅̉͒͑͋̿̓̾̌̚I̷͍̟̱̫͎͎̪͕̭̳̩̬͙̅̓̄̈̃̓̐͗̾̿̇̚學҈̪̜͙͙͍̪̟̠͓͚͈͇̀̂͌̂̆̈́̓͌̊̃̂̋̇̐̿̂͗͊̂程҉͉̣̱̱̜͍̥̥̤̙̾̅̀̂̌͛̅͆̓̎͗̅̂"-開發者李哲維','即將消失的學程"A̸̡̛͓̘̟͍̣̎̽͐҈̴̷̢͙̖͇̖͈̟̩̑̀̓̿҇́́̈̕͢ͅͅ҈̧͇͙͎̥͊̂̂͗̚͞҉̛̭̬̜̩̄͐͆̅̅͢҈̵̴̷̶̢̧̧̢̦̰̬̪̫͎̝͔̜͙̟͎̯̝̟̟̙̫̿̍̋҇̽̃́̿͗̇̌̄̍̏̋̈̔̒̌́͆̄̉͑̍̕̕͜͡͠҈̴̵̢̡̛̘̜̣̬̙͇͈̜̟҇̍͛̈́҇̾̈́̊̔̈́̎͌͒̆̈͢҉̷̡̡̜̲͉͇̗͙̀̊́̾̌̓́͞͞҈̧͕̲͖̫͌̆͆͠҉̩͓͚͓̬͆͂̎̅͑̕͢҉̷̸̸̷̷̧̧̨̟̦̱͎̙̫͖͇̲͈͎͍͈̩̦̥̟̜̠̤̥̜͖̬̠͔̞͍̂̊̒҇̐̒̌̅̊̈́͊̌̎̈͋͋̈́͗̿̏̒̀̚̚̚͢͢͜͠͠͡͡͝҉̵̴̡̨͎͔̜̗͈̙̤͖̪̞̳̙̱͚҇̔͗̽̓̒̇̿̐̐̕͜͝ͅ҈̰͔̮̭̠̙҇͑̋͑͋͜҈̠̣̄̏͐̕͢ͅ҉̢̲̖̊̊̿̑̕I҈̶̴̵̴̶̨̡̧̢̨̛͚͖̮̫̗̦͍͉̰̫̖̘̮̜͓̏̉̀͊̓̋͗̆͒̈҇́͐̀͋̊͑҇̾̆̆̋̇͊̀̊͠͡҈̸̢̮͓̱̝̔̂̓͗̽̎̊̐̚͜͠͞҉̵̧̨̯̟͚̮̯͉̞̅̂̈́̑҇̏̋͊́͡҉̡̮̟̙͛͆̿͌͠҉̶̵̵̷̷̸̸̧̢̨̧̛̛̖̩̯͈̘̙̞͍̗͉̬͉͕͚̜̖̲̝̣͇̦̘̳͈͇̪̥̤͂̇͌̋̆̃̌̔̔̓̈͒̽̈͌̊̔̄̎̑̂̀̐̓҇̀̈̈́̑͑̓̂͜͢͢͢͝͞͞͠͞ͅ҈̶̴̴̸̷̸̧̧̧̜̲̘͖̖͕̲͍̞͈͖̫̬͈̫̥̬̩̟͉͚̙͚͎͕̱͒̊̈́҇͐̾̎̈̀̔̽̿͛̏̅͌͆̒͌͐̏͛́͋̎̅̇̈̂̈́̔̚̚̕͢͜͢͜͞͞͠͡͠҉̸̧̧̣͉͔̬̮͕̑̉̉̐͠͡學̶̡͔͖̓̃͑͡҉҈̶̨̢̛̦̙̙͙̣̭̩̫̋̿͂͛͐҇̎͆̿̏̿̾҉̨͚̫̇͛͊̋̕҈̴̧̛͓̮͉̤͎̝̩͌͌͂̑̌҇̓̀̇͢҉̵̴̷̴̷̨̧̢̡̟̰̫̜̣̳̟̥̙̦̭͍̟͙̟̝̝͇̪̯̠͎̠҇̆̓͂̑͂̋́̏̈̎̅̃̿̆̈̎͌̊͗̐͢͜͠͡͝͠͡ͅ҉̴̧̠̟̪̪͚̝͖͉̰͉҇͗̋̉̓̒͑͂̕͢ͅͅ҉̨̙̘͈̣̉̀̓̓̍͝҈̡̞̩̪̣̇̊͠҈̢̛̠͓̙̿̀̀͋̚҉̡̪̱͍͙͕͖̓͊͞҈̵̸̨̡͕̮̝̞͎͕̬̩̪͉̱͔̫̲̫̜̾̈͋͑̿̀̀̄́̓͜͝͞͞程҈̧̥̱͍̤҇̎̏͌͐̃ͅ҈̴̡̛̠̜͖̽͒͂̕҉̸̧̧̲͍̦̤̬͑̄͆̀͆͊̇̚͢͞͝ͅ҈̟͖̤͉͛̆͗͛͢͞҉̢̘͖̬̜̙̈̉̈́̈͆͡҉̶̢̡̟̖͙̳̠̥̟̬͙͔͒̈́̎̎̕͡҈̞͓̗̬̮̰̇̏͢͡҈̵̧̜̠͎͇̘͈͓̮̞͗̂̀͆̈́҇̀̃̃͢͡"\n開發者-李哲維']), gv.g.current_user.student_id, random.choice(['恭喜你發現彩蛋，照我RRRRRRRR，照顧I҈̶̴̵̴̶̨̡̧̢̨̛͚͖̮̫̗̦͍͉̰̫̖̘̮̜͓̏̉̀͊̓̋͗̆͒̈҇́͐̀͋̊͑҇̾̆̆̋̇͊̀̊͠͡҈̸̢̮͓̱̝̔̂̓͗̽̎̊̐̚͜͠͞҉̵̧̨̯̟͚̮̯͉̞̅̂̈́̑҇̏̋͊́͡҉̡̮̟̙͛͆̿͌͠҉̶̵̵̷̷̸̸̧̢̨̧̛̛̖̩̯͈̘̙̞͍̗͉̬͉͕͚̜̖̲̝̣͇̦̘̳͈͇̪̥̤͂̇͌̋̆̃̌̔̔̓̈͒̽̈͌̊̔̄̎̑̂̀̐̓҇̀̈̈́̑͑̓̂͜͢͢͢͝͞͞͠͞ͅ҈̶̴̴̸̷̸̧̧̧̜̲̘͖̖͕̲͍̞͈͖̫̬͈̫̥̬̩̟͉͚̙͚͎͕̱͒̊̈́҇͐̾̎̈̀̔̽̿͛̏̅͌͆̒͌͐̏͛́͋̎̅̇̈̂̈́̔̚̚̕͢͜͢͜͞͞͠͡͠҉̸̧̧̣͉͔̬̮͕̑̉̉̐͠͡學̶̡͔͖̓̃͑͡拜託大家了','推薦你去聽草東\nhttps://www.youtube.com/watch?v=SB3_m1jU-BU&pp=ygUG5p-T57y4','推薦你去聽\nhttps://youtu.be/-oDRzgmYHms?list=RD-oDRzgmYHms&t=76']))
    return [lineSDK.FlexSendMessage(alt_text="開發者-李哲維", contents=developer.zhe())]


@Dialog_Manager.bind('huan')
def easter_egg():
    return [lineSDK.FlexSendMessage(alt_text="開發者-李念寰", contents=developer.huan())]

@Dialog_Manager.bind('海棠')
def easter_egg():
    return [lineSDK.FlexSendMessage(alt_text="開發者-徐海棠", contents=developer.dona())]

@Dialog_Manager.bind('yh')
def easter_egg():
    return [lineSDK.FlexSendMessage(alt_text="指導教授-吳宜鴻", contents=developer.yh())]


@Dialog_Manager.bind('henry')
def easter_egg():
    return [lineSDK.FlexSendMessage(alt_text="特別感謝", contents=developer.henry())]


Q_and_A_excel()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
