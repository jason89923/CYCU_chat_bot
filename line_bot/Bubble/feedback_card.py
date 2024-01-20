import global_variable as gv
def feedback_card():

    res = {
        "type": "bubble",
        "size": "mega",
        "direction": "ltr",
        "header": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "text",
                    "text": "意見回饋",
                    "color": "#000000",
                    "size": "xl",
                    "weight": "bold",
                    "style": "normal",
                    "align": "center",
                    "offsetTop": "xs"
                }
            ],
            "paddingAll": "lg",
            "justifyContent": "center",
            "alignItems": "center",
            "backgroundColor": "#FFFFFF"
        },
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
                            "action": {
                                "type": "message",
                                "label": "校方回饋",
                                "text": "校方回饋"
                            },
                            "url": f"{gv.URL}Feedback/school.png"
                        },
                        {
                            "type": "image",
                            "action": {
                                "type": "message",
                                "label": "常見問題",
                                "text": "常見問題"
                            },
                            "url": f"{gv.URL}Feedback/question.png"
                        }
                    ]
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "image",
                            "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": "https://docs.google.com/forms/d/e/1FAIpQLSfc2Z0DTO5ofrKN3UA_tG2QbF4kUsMXUVbJLphJWOgqxEBW5g/viewform"
                            },
                            "url": f"{gv.URL}Feedback/form.png"
                        },
                        {
                            "type": "image",
                            "url": f"{gv.URL}Feedback/system.png",
                            "action": {
                                "type": "message",
                                "label": "系統改善",
                                "text": "系統改善"
                            }
                        }
                    ]
                }
            ],
            "spacing": "none",
            "background": {
                "type": "linearGradient",
                "angle": "045deg",
                "startColor": "#CCCCCC4C",
                "endColor": "#CCCCCC26"
            },
            "position": "relative",
            "margin": "none"
        },
        "styles": {
            "header": {
                "backgroundColor": "#D57474FF"
            }
        }
    }

    return res
