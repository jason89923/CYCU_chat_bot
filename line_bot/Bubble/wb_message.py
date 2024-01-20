import global_variable as gv
def wb_message_card(message_num):
    if message_num > 10:
        message_num = 10
    res = {
        "type": "bubble",
        "size": "mega",
        "body": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "image",
                    "url": f"{gv.URL}bubble/water_ballon_{message_num}.png",
                    "size": "full"
                }
            ],
            "paddingAll": "none",
            "alignItems": "center",
            "height": "100px",
            "action": {
                "type": "message",
                "label": "action",
                "text": "查看未讀訊息"
            }
        }
    }

    return res



