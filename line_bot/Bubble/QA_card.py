import global_variable as gv
def make_question_card(title, content):
    res = {
        "type": "bubble",
        "size": "kilo",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "image",
                            "url": f"{gv.URL}bubble/Q.png",
                            "size": "sm"
                        },
                        {
                            "type": "text",
                            "text": title,
                            "size": "xl",
                            "align": "center",
                            "wrap": True,
                            "weight": "bold",
                            "color": "#000000",
                            "adjustMode": "shrink-to-fit"
                        }
                    ],
                    "justifyContent": "center",
                    "alignItems": "center"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": content,
                            "wrap": True,
                            "weight": "bold",
                            "color": "#000000"
                        }
                    ],
                    "paddingAll": "xxl",
                    "background": {
                        "type": "linearGradient",
                        "angle": "0deg",
                        "startColor": "#E2E0CF68",
                        "endColor": "#ffffff"
                    },
                    "cornerRadius": "xxl"
                }
            ],
            "background": {
                "type": "linearGradient",
                "angle": "180deg",
                "startColor": "#E9D7361E",
                "endColor": "#E9763668"
            },
            "spacing": "xl",
            "borderWidth": "bold",
            "paddingAll": "xl",
            "justifyContent": "space-around",
            "action": {
                "type": "message",
                "label": "action",
                "text": content
            }
        },
        "styles": {
            "header": {
                "backgroundColor": "#F88EBB"
            }
        }
    }

    return res


def make_answer_card(title, content, link):
    res = {
        "type": "bubble",
        "size": "mega",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "image",
                            "url": f"{gv.URL}bubble/A.png",
                            "size": "sm"
                        },
                        {
                            "type": "text",
                            "text": title,
                            "size": "xl",
                            "align": "center",
                            "wrap": True,
                            "weight": "bold",
                            "color": "#000000",
                            "adjustMode": "shrink-to-fit"
                        }
                    ],
                    "justifyContent": "center",
                    "alignItems": "center"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": content,
                            "wrap": True,
                            "weight": "bold",
                            "color": "#000000"
                        }
                    ],
                    "paddingAll": "xxl",
                    "background": {
                        "type": "linearGradient",
                        "angle": "0deg",
                        "startColor": "#E2E0CF68",
                        "endColor": "#ffffff"
                    },
                    "cornerRadius": "xxl"
                }
            ],
            "background": {
                "type": "linearGradient",
                "angle": "135deg",
                "startColor": "#FFD6BF68",
                "endColor": "#79D32868"
            },
            "spacing": "xl",
            "borderWidth": "bold",
            "paddingAll": "xl",
            "justifyContent": "space-around",
            **({'action': {
                "type": "uri",
                "label": "action",
                "uri": link
            }} if link is not None else {})
        },
        "styles": {
            "header": {
                "backgroundColor": "#F88EBB"
            }
        }
    }

    return res


def make_type_card(type):
    res = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "image",
                    "url": f"{gv.URL}Feedback/QA_bg.png",
                    "size": "full"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": type,
                            "size": "4xl",
                            "weight": "bold"
                        }
                    ],
                    "position": "absolute",
                    "width": "100%",
                    "paddingAll": "none",
                    "offsetTop": "45%",
                    "offsetStart": "20%"
                }
            ],
            "paddingAll": "none",
            "action": {
                "type": "message",
                "label": "action",
                "text": type
            }
        }
    }
    return res
