def water_polo_card(std_id, text, curriculum, subscription_list):
    res = {
        "type": "bubble",
        "size": "kilo",
        "header": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "目標 : ",
                            "weight": "bold",
                            "adjustMode": "shrink-to-fit",
                            "align": "start",
                            "size": "lg"
                        }
                    ],
                    "width": "30%",
                    "alignItems": "center",
                    "justifyContent": "center"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": std_id if std_id != [] else "請輸入學號......",
                            "align": "start",
                            "action": {
                                "type": "message",
                                "label": "action",
                                "text": "丟水球-學號"
                            }
                        }
                    ],
                    "background": {
                        "type": "linearGradient",
                        "angle": "0deg",
                        "startColor": "#B2B2B266",
                        "endColor": "#ffffff"
                    },
                    "margin": "none",
                    "paddingAll": "sm",
                    "cornerRadius": "xl",
                    "paddingStart": "lg",
                    "action": {
                        "type": "message",
                        "label": "action",
                        "text": "丟水球-學號"
                    }
                }
            ],
            "background": {
                "type": "linearGradient",
                "angle": "135deg",
                "startColor": "#8AA1C272",
                "endColor": "#72FFEC72"
            }
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
                            "type": "text",
                            "text": "📌訊息",
                            "weight": "bold"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "清除",
                                    "align": "center",
                                    "size": "sm",
                                    "weight": "bold"
                                }
                            ],
                            "action": {
                                "type": "message",
                                "label": "action",
                                "text": "丟水球-清除訊息"
                            },
                            "cornerRadius": "xl",
                            "background": {
                                "type": "linearGradient",
                                "angle": "0deg",
                                "startColor": "#E18095A6",
                                "endColor": "#E8E8E8"
                            },
                            "maxWidth": "25%",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "offsetEnd": "md",
                            "paddingAll": "md"
                        }
                    ],
                    "alignItems": "center",
                    "paddingAll": "md"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": text if text != [] else "請輸入訊息.....",
                            "wrap": True
                        }
                    ],
                    "borderWidth": "light",
                    "borderColor": "#858585FF",
                    "cornerRadius": "md",
                    "backgroundColor": "#ffffff",
                    "width": "90%",
                    "paddingAll": "lg",
                    "paddingBottom": "xxl",
                    "action": {
                        "type": "message",
                        "label": "action",
                        "text": "丟水球-訊息"
                    },
                    "paddingAll": "md"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "📌功課表",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "☑" if curriculum != [] else "□",
                            "size": "xl",
                            "align": "end",
                            "offsetEnd": "lg"
                        }
                    ],
                    "alignItems": "center",
                    "action": {
                        "type": "message",
                        "label": "action",
                        "text": "丟水球-功課表"
                    },
                    "paddingAll": "md"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "📌追蹤清單",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "☑" if subscription_list != [] else "□",
                            "size": "xl",
                            "align": "end",
                            "offsetEnd": "lg"
                        }
                    ],
                    "alignItems": "center",
                    "action": {
                        "type": "message",
                        "label": "action",
                        "text": "丟水球-追蹤清單"
                    },
                    "paddingAll": "md"
                }
            ],
            "backgroundColor": "#ffffff",
            "paddingBottom": "none"
        },
        "footer": {
            "type": "box",
            "layout": "horizontal",
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
                        "text": "丟水球-送出"
                    },
                    "offsetStart": "xxl",
                    "alignItems": "center",
                    "justifyContent": "center"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "謹言慎行",
                            "size": "sm",
                            "color": "#FF0000",
                            "align": "end",
                            "weight": "bold"
                        }
                    ],
                    "justifyContent": "flex-end",
                    "offsetTop": "sm",
                    "width": "25%",
                    "offsetStart": "xxl",
                    "action": {
                        "type": "message",
                        "label": "action",
                        "text": "謹言慎行"
                    }
                }
            ],
            "alignItems": "center",
            "justifyContent": "center",
            "action": {
                "type": "message",
                "label": "action",
                "text": "丟水球-送出"
            },
            "offsetStart": "lg",
            "spacing": "xl"
        },
        "styles": {
            "body": {
                "backgroundColor": "#C0C0C07F"
            }
        }
    }
    return res
