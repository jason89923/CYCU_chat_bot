import requests
import json
from linebot import LineBotApi
import global_variable as gv

line_bot_api = LineBotApi(gv.LINE_CHANNEL.ACCESS_TOKEN)


# 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
headers = {'Authorization': 'Bearer ' + gv.LINE_CHANNEL.ACCESS_TOKEN, 'Content-Type': 'application/json'}

body = {
    'size': {'width': 2500, 'height': 1686},   # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'main',                   # 選單名稱
    'chatBarText': '選單',            # 選單在 LINE 顯示的標題
    'areas': [                                  # 選單內容
        {
            'bounds': {'x': 50, 'y': 185, 'width': 850, 'height': 535},
            'action': {'type': 'message', 'text': '查詢課程'}
        },
        {
            'bounds': {'x': 1005, 'y': 185, 'width': 850, 'height': 535},
            'action': {'type': 'message', 'text': '畢業門檻'}
        },
        {
            'bounds': {'x': 50, 'y': 933, 'width': 679, 'height': 663},
            'action': {'type': 'message', 'text': '功課表'}
        },
        {
            'bounds': {'x': 783, 'y': 933, 'width': 679, 'height': 663},
            'action': {'type': 'message', 'text': '追蹤清單'}
        },
        {
            'bounds': {'x': 1567, 'y': 933, 'width': 679, 'height': 663},
            'action': {'type': 'message', 'text': '意見回饋'}
        },
        {
            'bounds': {'x': 1967, 'y': 417, 'width': 500, 'height': 500},
            'action': {'type': 'message', 'text': '丟水球'}
        }
    ]
}

# 向指定網址發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                       headers=headers, data=json.dumps(body).encode('utf-8'))
# 印出得到的結果
print(req.text)
# 設定選單背景
with open('/home/tliw1/Cycu_line_bot/line_bot/image/menu.png', 'rb') as f:
    line_bot_api.set_rich_menu_image('richmenu-1cc6b32fd119ad5588a67fbe41c28df9', 'image/jpeg', f)


# # # 顯示圖文選單
req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-1cc6b32fd119ad5588a67fbe41c28df9', headers=headers)
print(req.text)


'''
response = requests.delete('https://api.line.me/v2/bot/richmenu/richmenu-afb3cd620e49fbd469ed589a0cce1bad', headers=headers)

if response.status_code == 200:
    print('Rich menu deleted successfully.')
else:
    print('Failed to delete rich menu. Error code: ' + str(response.status_code))
'''
