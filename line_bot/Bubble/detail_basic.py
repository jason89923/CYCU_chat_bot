def pass_card(course_type, name, score, id, credit, year):
    res = {
        "type": "bubble",
        "size": "kilo",
        "header": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "text",
                    "text": f" 🅘 {course_type}",
                    "size": "lg",
                    "align": "center",
                    "weight": "bold",
                    "wrap": True,
                    "color": "#ffffff"
                }
            ],
            "paddingAll": "xxl",
            "background": {
                "type": "linearGradient",
                "angle": "160deg",
                "startColor": "#7C899BCC",
                "endColor": "#828282B9"
            }
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
                            "text": f"★ {name}",
                            "size": "md",
                            "weight": "bold",
                            "style": "normal"
                        }
                    ],
                    "paddingAll": "sm"
                },
                {
                    "type": "separator",
                    "color": "#000000"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "◎ 課程代碼",
                                                    "size": "md",
                                                    "adjustMode": "shrink-to-fit",
                                                    "weight": "bold"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": id,
                                                    "size": "md",
                                                    "adjustMode": "shrink-to-fit",
                                                    "align": "end"
                                                }
                                            ],
                                            "width": "40%"
                                        }
                                    ],
                                    "alignItems": "center"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "◎ 學分數",
                                                    "size": "md",
                                                    "adjustMode": "shrink-to-fit",
                                                    "weight": "bold"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": credit,
                                                    "size": "md",
                                                    "adjustMode": "shrink-to-fit",
                                                    "align": "end"
                                                }
                                            ],
                                            "width": "20%"
                                        }
                                    ],
                                    "alignItems": "center"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "◎ 通過學期",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "adjustMode": "shrink-to-fit"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": year,
                                                    "size": "md",
                                                    "wrap": True,
                                                    "align": "end"
                                                }
                                            ],
                                            "alignItems": "flex-end",
                                            "width": "25%"
                                        }
                                    ],
                                    "alignItems": "center"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "◎ 分數",
                                                    "size": "md",
                                                    "adjustMode": "shrink-to-fit",
                                                    "weight": "bold"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": score,
                                                    "size": "md",
                                                    "adjustMode": "shrink-to-fit",
                                                    "align": "end"
                                                }
                                            ],
                                            "width": "40%"
                                        }
                                    ],
                                    "alignItems": "center"
                                }
                            ],
                            "paddingAll": "md",
                            "borderWidth": "semi-bold",
                            "borderColor": "#A6A6A6",
                            "cornerRadius": "xl",
                            "backgroundColor": "#EBEBEB"
                        }
                    ],
                    "paddingBottom": "md",
                    "paddingTop": "md"
                }
            ],
            "paddingTop": "lg",
            "paddingBottom": "none"
        },
        "footer": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "僅供參考",
                            "size": "xxs",
                            "weight": "bold",
                            "align": "center",
                            "color": "#767676",
                            "action": {
                                "type": "message",
                                "label": "action",
                                "text": "僅供參考"
                            }
                        }
                    ],
                    "width": "30%",
                    "paddingAll": "sm"
                }
            ],
            "alignItems": "flex-end",
            "justifyContent": "flex-end",
            "paddingAll": "none"
        }
    }
    return res


def fail_card(course_type, name):
    res = {
        "type": "bubble",
        "size": "kilo",
        "header": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "text",
                    "text": f" 🅘 {course_type}",
                    "size": "lg",
                    "align": "center",
                    "weight": "bold",
                    "wrap": True,
                    "color": "#ffffff"
                }
            ],
            "paddingAll": "xxl",
            "background": {
                "type": "linearGradient",
                "angle": "160deg",
                "startColor": "#7C899BCC",
                "endColor": "#828282B9"
            }
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
                            "text": f"★ {name}",
                            "size": "md",
                            "weight": "bold",
                            "style": "normal"
                        }
                    ],
                    "paddingAll": "sm"
                },
                {
                    "type": "separator",
                    "color": "#000000"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "✘ 尚未修習",
                                    "align": "center",
                                    "weight": "bold",
                                    "color": "#626262",
                                    "size": "xl"
                                }
                            ],
                            "paddingAll": "xl",
                            "cornerRadius": "md",
                            "width": "80%",
                            "backgroundColor": "#C6C6C6"
                        }
                    ],
                    "alignItems": "center",
                    "justifyContent": "center",
                    "paddingAll": "xl",
                    "paddingTop": "xxl"
                }
            ],
            "paddingTop": "lg",
            "paddingBottom": "none"
        },
        "footer": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "僅供參考",
                            "size": "xxs",
                            "weight": "bold",
                            "align": "center",
                            "color": "#767676",
                            "action": {
                                "type": "message",
                                "label": "action",
                                "text": "僅供參考"
                            }
                        }
                    ],
                    "width": "30%",
                    "paddingAll": "sm"
                }
            ],
            "alignItems": "flex-end",
            "justifyContent": "flex-end",
            "paddingAll": "none"
        }
    }
    return res
