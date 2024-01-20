def system_opinion_card(text):
    res = {
        "type": "bubble",
        "size": "kilo",
        "header": {
            "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "⚙️系統改善",
                        "weight": "bold",
                        "adjustMode": "shrink-to-fit",
                        "align": "center",
                        "size": "lg"
                    }
                ],
            "background": {
                    "type": "linearGradient",
                    "angle": "135deg",
                    "startColor": "#A6C3E4CC",
                    "endColor": "#91C6B0AC"
                    },
            "alignItems": "center"
        },
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
                            "text": "📝請輸入系統改善建議",
                            "weight": "bold",
                            "align": "start",
                            "offsetEnd": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": text if text != [] else "請輸入建議......",
                                    "wrap": True
                                }
                            ],
                            "borderWidth": "light",
                            "borderColor": "#858585FF",
                            "cornerRadius": "md",
                            "backgroundColor": "#ffffff",
                            "width": "90%",
                            "paddingAll": "xxl",
                            "action": {
                                "type": "message",
                                "label": "action",
                                "text": "系統改善-建議"
                            },
                        }
                    ],
                    "borderWidth": "medium",
                    "borderColor": "#858585FF",
                    "cornerRadius": "lg",
                    "backgroundColor": "#ffffff",
                    "alignItems": "center",
                    "paddingAll": "lg"
                }
            ],
            "margin": "md"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": " 送出 ",
                                "size": "sm",
                                "align": "center",
                                "weight": "bold"
                            }
                        ],
                        "paddingAll": "md",
                        "cornerRadius": "xxl",
                        "width": "40%",
                        "background": {
                            "type": "linearGradient",
                            "angle": "0deg",
                            "startColor": "#9C94FF72",
                            "endColor": "#E9E9E9FF"
                        },
                        "action": {
                            "type": "message",
                            "label": "action",
                            "text": "系統改善-送出"
                        }
                    }
            ],
            "alignItems": "center",
            "justifyContent": "center",
            "action": {
                "type": "message",
                "label": "action",
                "text": "系統改善-送出"
            }
        },
        "styles": {
            "body": {
                "backgroundColor": "#C0C0C07F"
            }
        }
    }

    return res
