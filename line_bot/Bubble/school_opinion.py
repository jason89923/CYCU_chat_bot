import global_variable as gv
def school_opinion_card(id, img):
    res = {
        "type": "bubble",
        "size": "kilo",
        "hero": {
            "type": "image",
            "url": f"{gv.URL}Feedback/{img}.png",
            "margin": "none",
            "size": "full"
        },
        "action": {
            "type": "uri",
            "label": "action",
            "uri": f"https://itouch.cycu.edu.tw/active_project/cycu2000h_02/cycu_05/?id={id}"
        }
    }
    return res


def carousel():
    list = ['43', '44', '45', '46', '47', '48', '49', '50', '51']
    img = ['school_1', 'school_2', 'school_3', 'school_4', 'school_5', 'school_6', 'school_7', 'school_8', 'school_9']
    opinion_bubble = []

    for i in range(len(list)):
        opinion_bubble.append(school_opinion_card(list[i], img[i]))

    res = {
        "type": "carousel",
        "contents": opinion_bubble
    }
    return res
