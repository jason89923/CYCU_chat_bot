def next_page_card(text):
    res = {
        "type": "bubble",
        "size": "mega",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": ">",
                            "size": "5xl",
                            "color": "#777777FF",
                            "offsetBottom": "xs"
                        }
                    ],
                    "justifyContent": "center",
                    "alignItems": "center",
                    "borderWidth": "bold",
                    "borderColor": "#777777FF",
                    "cornerRadius": "90px",
                    "width": "60%",
                    "action": {
                        "type": "message",
                        "label": f"{text}下一頁",
                        "text": f"{text}下一頁"
                    }
                }
            ],
            "justifyContent": "center",
            "alignItems": "center",
            "backgroundColor":"#00000000"
        }
    }
    return res


def next_page_card_detail(text):
    res = {
        "type": "bubble",
        "size": "kilo",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": ">",
                            "size": "5xl",
                            "color": "#777777FF",
                            "offsetBottom": "xs"
                        }
                    ],
                    "justifyContent": "center",
                    "alignItems": "center",
                    "borderWidth": "bold",
                    "borderColor": "#777777FF",
                    "cornerRadius": "90px",
                    "width": "60%",
                    "action": {
                        "type": "message",
                        "label": f"{text}下一頁",
                        "text": f"{text}下一頁"
                    }
                }
            ],
            "justifyContent": "center",
            "alignItems": "center",
            "backgroundColor":"#00000000"
        }
    }
    return res
