
import global_variable as gv
def eng_bubble(eng_all_class, eng_test):
    eng_all_class_list = eng_all_class['dataList']
    eng_test_list = eng_test['dataList']
    res = {
        "type": "bubble",
        "size": "micro",
        "direction": "ltr",
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
                            "text": "🎓",
                            "size": "lg",
                            "align": "center",
                            "weight": "bold",
                            "wrap": True
                        }
                    ],
                    "width": "20%"
                },
                {
                    "type": "text",
                    "text": "全英文課程",
                    "size": "md",
                    "align": "center",
                    "weight": "bold",
                    "wrap": True
                }
            ],
            "paddingAll": "lg",
            "background": {
                "type": "linearGradient",
                "angle": "35deg",
                "startColor": "#B58989A1",
                "endColor": "#98C1D572"
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
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "◆ 應修",
                                            "size": "sm",
                                            "weight": "bold",
                                        }
                                    ],
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": '2 (門)',
                                            "size": "xs"
                                        }
                                    ],
                                    "alignItems": "flex-end",
                                }
                            ],
                            "paddingAll": "sm"
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
                                            "text": "◆ 已修",
                                            "size": "sm",
                                            "weight": "bold",
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": f'{len(eng_all_class_list)} (門)',
                                            "size": "xs"
                                        }
                                    ],
                                    "alignItems": "flex-end",
                                }
                            ],
                            "paddingAll": "sm",
                            "paddingBottom": "lg"
                        },

                    ]
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
                                    "text": "★ 英文能力檢定",
                                    "size": "md",
                                    "weight": "bold",
                                    "style": "italic"
                                }
                            ]
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
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "通過" if len(eng_test_list) > 0 else "未通過",
                                                            "size": "md",
                                                            "weight": "bold",
                                                            "adjustMode": "shrink-to-fit",
                                                            "align": "center",
                                                            "color": "#4A9025FF"if len(eng_test_list) > 0 else "#AE3532FF"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "paddingBottom": "md",
                            "paddingTop": "lg"
                        }
                    ]
                }
            ],
            "paddingTop": "xxl",
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
                            "align": "start",
                            "color": "#767676",
                            "action": {
                                "type": "message",
                                "label": "action",
                                "text": "僅供參考"
                            }
                        }
                    ],
                    "width": "50%",
                    "paddingAll": "sm"
                }
            ],
            "alignItems": "flex-end",
            "justifyContent": "flex-end",
            "paddingAll": "none"
        }
    }
    return res


def bubble(result, keyword):
    result_list = list(sorted(result.items()))
    if result_list[0][0] == 'DT_chose':
        type = '學系選修'
    elif result_list[0][0] == 'DT_must':
        type = '學系必修'
    elif result_list[0][0] == 'KNOWLEDGH':
        type = '基本知能'
    elif result_list[0][0] == 'GE_LIST':
        type = '基礎必修通識'
    elif result_list[0][0] == 'GE_XTEND':
        type = '延伸選修通識'
    res = {
        "type": "bubble",
        "size": "micro",
        "direction": "ltr",
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
                                "text": "🎓",
                                "size": "lg",
                                "align": "center",
                                "weight": "bold",
                                "wrap": True
                            }
                        ],
                        "width": "20%",
                        "action": {
                            "type": "message",
                            "label": "action",
                            "text": keyword
                        }
                    },
                {
                        "type": "text",
                        "text": type,
                        "size": "md",
                        "align": "center",
                        "weight": "bold",
                        "wrap": True
                        }
            ],
            "paddingAll": "lg",
            "background": {
                "type": "linearGradient",
                "angle": "180deg",
                "startColor": "#C3B95D60" if result_list[1][1] >= result_list[0][1] else "#97576760",
                "endColor": "#99DC3760" if result_list[1][1] >= result_list[0][1] else "#D75A5A60",
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
                                                    "text": "◆ 應修學分",
                                                    "size": "sm",
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
                                                    "text": str(result_list[0][1]),
                                                    "size": "sm",
                                                    "wrap": True,
                                                    "align": "end"
                                                }
                                            ],
                                            "alignItems": "flex-end",
                                            "width": "20%"
                                        }
                                    ],
                                    "paddingAll": "sm"
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
                                                    "text": "◆ 已修學分",
                                                    "size": "sm",
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
                                                    "text": str(result_list[1][1]),
                                                    "size": "sm",
                                                    "adjustMode": "shrink-to-fit",
                                                    "align": "end"
                                                }
                                            ],
                                            "width": "20%"
                                        }
                                    ],
                                    "paddingAll": "sm"
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
                                                    "text": "◆ 正在修習",
                                                    "size": "sm",
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
                                                    "text": str(result_list[2][1]),
                                                    "size": "sm",
                                                    "adjustMode": "shrink-to-fit",
                                                    "align": "end"
                                                }
                                            ],
                                            "width": "20%"
                                        }
                                    ],
                                    "paddingAll": "sm"
                                }
                            ]
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
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "💡",
                            "size": "lg"
                        },
                        {
                            "type": "text",
                            "text": "推薦課程",
                            "size": "xxs"
                        }
                    ],
                    "justifyContent": "center",
                    "alignItems": "center",
                    "borderWidth": "semi-bold",
                    "borderColor": "#6E6E6E89",
                    "margin": "sm",
                    "cornerRadius": "15px",
                    "paddingAll": "none",
                    "background": {
                        "type": "linearGradient",
                        "angle": "35deg",
                        "startColor": "#B58989A1",
                        "endColor": "#98C1D572"
                    },
                    "action": {
                        "type": "message",
                        "label": f"推薦{type}課程",
                        "text": f"推薦{type}課程"
                    }
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "🅘",
                            "size": "lg"
                        },
                        {
                            "type": "text",
                            "text": "詳細資訊",
                            "size": "xxs"
                        }
                    ],
                    "justifyContent": "center",
                    "alignItems": "center",
                    "borderWidth": "semi-bold",
                    "borderColor": "#6E6E6E89",
                    "cornerRadius": "15px",
                    "margin": "sm",
                    "background": {
                        "type": "linearGradient",
                        "angle": "35deg",
                        "startColor": "#B58989A1",
                        "endColor": "#98C1D572"
                    },
                    "action": {
                        "type": "message",
                        "label": f"{type}詳細資訊",
                        "text": f"{type}詳細資訊"
                    }
                }
            ],
            "margin": "none",
            "paddingAll": "md",
            "paddingStart": "xs",
            "paddingEnd": "xs"
        }
    }

    return res


def detail():
    res = {
        "type": "bubble",
        "size": "micro",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "image",
                    "url": f"{gv.URL}bubble/other.png",
                    "size": "full",
                    "action": {
                        "type": "message",
                        "label": "其他修課紀錄",
                        "text": "其他修課紀錄"
                    },
                    "position": "relative",
                    "align": "end"
                }
            ],
            "paddingAll": "none",
            "backgroundColor": "#E4FFED",
            "justifyContent": "center"
        },
        "styles": {
            "hero": {
                "backgroundColor": "#DDDDDD"
            }
        }
    }

    return res


def carousel(result):
    keyword = ['亮', 'gu', 'zhe', 'huan', 'yh']
    list = ['GE_XTEND', 'GE_LIST', 'KNOWLEDGH', 'DEPT_CHOOSE', 'DEPT_MUST']
    result = result['st_sum']
    graduation_bubble = []

    for i in range(len(list)):
        if (pass_or_not(result[list[i]])):
            graduation_bubble.append(bubble(result[list[i]], keyword[i]))
        else:
            graduation_bubble.insert(0, bubble(result[list[i]], keyword[i]))

    graduation_bubble.insert(0, eng_bubble(result['ENGLISH_ALL_CLASS'], result['ENGLISH_TEST']))
    graduation_bubble.append(detail())
    res = {
        "type": "carousel",
        "contents": graduation_bubble
    }
    return res


def pass_or_not(type_result):
    result_list = list(sorted(type_result.items()))
    if (result_list[1][1] >= result_list[0][1]):
        return True
    return False
