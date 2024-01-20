def cond_result(condition: dict, num_of_result=-1, current_page=-1, total_page=-1):
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
                    "text": "【查詢條件】",
                    "color": "#FFFFFF",
                    "size": "xl",
                    "weight": "bold",
                    "style": "normal",
                    "align": "start",
                    "offsetTop": "xs"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "全部清空",
                            "size": "md",
                            "weight": "bold",
                            "align": "center",
                            "color": "#000000"
                        }
                    ],
                    "backgroundColor": "#FACF8C75",
                    "width": "40%",
                    "height": "80%",
                    "action": {
                        "type": "message",
                        "label": "全部清空",
                        "text": "清空所有條件"
                    },
                    "offsetTop": "sm",
                    "offsetEnd": "lg",
                    "cornerRadius": "60px"
                }
            ],
            "background": {
                "type": "linearGradient",
                "angle": "90deg",
                "startColor": "#D57474FF",
                "endColor": "#B2B2B2FF"
            },
            "paddingAll": "md"
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
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "★上課時段",
                                            "size": "lg",
                                            "align": "start",
                                            "margin": "sm",
                                            "style": "normal",
                                            "contents": [],
                                            "gravity": "center",
                                            "weight": "bold",
                                            "decoration": "underline"
                                        }
                                    ],
                                    "paddingAll": "none"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "新增",
                                            "offsetTop": "sm",
                                            "offsetStart": "none",
                                            "size": "15px",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#000000"
                                        }
                                    ],
                                    "backgroundColor": "#FF000033",
                                    "width": "20%",
                                    "action": {
                                        "type": "message",
                                        "label": "指定上課時段",
                                        "text": "指定上課時段"
                                    },
                                    "cornerRadius": "60px",
                                    "offsetTop": "xs",
                                    "offsetEnd": "xl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "清除",
                                            "offsetTop": "sm",
                                            "size": "15px",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#000000"
                                        }
                                    ],
                                    "backgroundColor": "#B2B2B266",
                                    "width": "20%",
                                    "action": {
                                        "type": "message",
                                        "label": "清除上課時段",
                                        "text": "清除上課時段"
                                    },
                                    "cornerRadius": "60px",
                                    "offsetTop": "xs",
                                    "offsetEnd": "sm"
                                }
                            ],
                            "offsetTop": "sm",
                            "spacing": "xxl",
                            "paddingBottom": "sm",
                            "paddingEnd": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": add_cond(condition['time'], '上課時段')
                        }
                    ],
                    "offsetBottom": "none",
                    "paddingStart": "lg",
                    "paddingEnd": "lg",
                    "paddingTop": "xs",
                    "paddingBottom": "xxl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "separator",
                            "color": "#000000",
                            "margin": "none"
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
                                            "type": "text",
                                            "text": "★課程類別",
                                            "size": "lg",
                                            "align": "start",
                                            "margin": "sm",
                                            "style": "normal",
                                            "contents": [],
                                            "gravity": "center",
                                            "weight": "bold",
                                            "decoration": "underline"
                                        }
                                    ],
                                    "paddingAll": "none"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "新增",
                                            "offsetTop": "sm",
                                            "offsetStart": "none",
                                            "size": "15px",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#000000"
                                        }
                                    ],
                                    "backgroundColor": "#FF000033",
                                    "width": "20%",
                                    "action": {
                                        "type": "message",
                                        "label": "指定課程類別",
                                        "text": "指定課程類別"
                                    },
                                    "cornerRadius": "60px",
                                    "offsetTop": "xs",
                                    "offsetEnd": "xl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "清除",
                                            "offsetTop": "sm",
                                            "size": "15px",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#000000"
                                        }
                                    ],
                                    "backgroundColor": "#B2B2B266",
                                    "width": "20%",
                                    "action": {
                                        "type": "message",
                                        "label": "清除課程類別",
                                        "text": "清除課程類別"
                                    },
                                    "cornerRadius": "60px",
                                    "offsetTop": "xs",
                                    "offsetEnd": "sm"
                                }
                            ],
                            "offsetTop": "sm",
                            "spacing": "xxl",
                            "paddingBottom": "sm",
                            "paddingEnd": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": add_cond(condition['type'], '課程類別')
                        }
                    ],
                    "offsetBottom": "none",
                    "paddingBottom": "lg",
                    "paddingStart": "lg",
                    "paddingEnd": "lg"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "separator",
                            "color": "#000000",
                            "margin": "none"
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
                                            "type": "text",
                                            "text": "★授課老師",
                                            "size": "lg",
                                            "align": "start",
                                            "margin": "sm",
                                            "style": "normal",
                                            "contents": [],
                                            "gravity": "center",
                                            "weight": "bold",
                                            "decoration": "underline"
                                        }
                                    ],
                                    "paddingAll": "none"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "新增",
                                            "offsetTop": "sm",
                                            "offsetStart": "none",
                                            "size": "15px",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#000000"
                                        }
                                    ],
                                    "backgroundColor": "#FF000033",
                                    "width": "20%",
                                    "action": {
                                        "type": "message",
                                        "label": "指定授課老師",
                                        "text": "指定授課老師"
                                    },
                                    "cornerRadius": "60px",
                                    "offsetTop": "xs",
                                    "offsetEnd": "xl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "清除",
                                            "offsetTop": "sm",
                                            "size": "15px",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#000000"
                                        }
                                    ],
                                    "backgroundColor": "#B2B2B266",
                                    "width": "20%",
                                    "action": {
                                        "type": "message",
                                        "label": "清除授課老師",
                                        "text": "清除授課老師"
                                    },
                                    "cornerRadius": "60px",
                                    "offsetTop": "xs",
                                    "offsetEnd": "sm"
                                }
                            ],
                            "offsetTop": "sm",
                            "spacing": "xxl",
                            "paddingBottom": "sm",
                            "paddingEnd": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": add_cond(condition['teacher'], '授課老師')
                        }
                    ],
                    "offsetBottom": "none",
                    "paddingAll": "lg"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "separator",
                            "color": "#000000",
                            "margin": "none"
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
                                            "type": "text",
                                            "text": "★課程名稱",
                                            "size": "lg",
                                            "align": "start",
                                            "margin": "sm",
                                            "style": "normal",
                                            "contents": [],
                                            "gravity": "center",
                                            "weight": "bold",
                                            "decoration": "underline"
                                        }
                                    ],
                                    "paddingAll": "none"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "新增",
                                            "offsetTop": "sm",
                                            "offsetStart": "none",
                                            "size": "15px",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#000000"
                                        }
                                    ],
                                    "backgroundColor": "#FF000033",
                                    "width": "20%",
                                    "action": {
                                        "type": "message",
                                        "label": "指定課程名稱",
                                        "text": "指定課程名稱"
                                    },
                                    "cornerRadius": "60px",
                                    "offsetTop": "xs",
                                    "offsetEnd": "xl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "清除",
                                            "offsetTop": "sm",
                                            "size": "15px",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#000000"
                                        }
                                    ],
                                    "backgroundColor": "#B2B2B266",
                                    "width": "20%",
                                    "action": {
                                        "type": "message",
                                        "label": "清除課程名稱",
                                        "text": "清除課程名稱"
                                    },
                                    "cornerRadius": "60px",
                                    "offsetTop": "xs",
                                    "offsetEnd": "sm"
                                }
                            ],
                            "offsetTop": "sm",
                            "spacing": "xxl",
                            "paddingBottom": "sm",
                            "paddingEnd": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": add_cond(condition['name'], '課程名稱')
                        }
                    ],
                    "offsetBottom": "none",
                    "paddingAll": "lg",
                    "paddingBottom": "xxl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "separator",
                            "color": "#000000",
                            "margin": "none"
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
                                            "type": "text",
                                            "text": "★開課學系",
                                            "size": "lg",
                                            "align": "start",
                                            "margin": "sm",
                                            "style": "normal",
                                            "contents": [],
                                            "gravity": "center",
                                            "weight": "bold",
                                            "decoration": "underline"
                                        }
                                    ],
                                    "paddingAll": "none"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "新增",
                                            "offsetTop": "sm",
                                            "offsetStart": "none",
                                            "size": "15px",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#000000"
                                        }
                                    ],
                                    "backgroundColor": "#FF000033",
                                    "width": "20%",
                                    "action": {
                                        "type": "message",
                                        "label": "指定開課學系",
                                        "text": "指定開課學系"
                                    },
                                    "cornerRadius": "60px",
                                    "offsetTop": "xs",
                                    "offsetEnd": "xl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "清除",
                                            "offsetTop": "sm",
                                            "size": "15px",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#000000"
                                        }
                                    ],
                                    "backgroundColor": "#B2B2B266",
                                    "width": "20%",
                                    "action": {
                                        "type": "message",
                                        "label": "清除開課學系",
                                        "text": "清除開課學系"
                                    },
                                    "cornerRadius": "60px",
                                    "offsetTop": "xs",
                                    "offsetEnd": "sm"
                                }
                            ],
                            "offsetTop": "sm",
                            "spacing": "xxl",
                            "paddingBottom": "xl",
                            "paddingEnd": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": add_cond(condition['department'], '開課學系'),
                            "paddingBottom": "lg",
                        }

                    ],
                    "offsetBottom": "none",
                    "paddingBottom": "lg",
                    "paddingStart": "lg",
                    "paddingEnd": "lg"
                },

            ],
            "offsetBottom": "none",
            "paddingAll": "none"
        }

    }
    if (num_of_result != -1):
        res["footer"] = {
            "type": "box",
            "layout": "vertical",
            "contents": add_result(num_of_result, current_page, total_page),
            "background": {
                "type": "linearGradient",
                "angle": "270deg",
                "startColor": "#D5747487",
                "endColor": "#B2B2B2FF"
            },
            "paddingAll": "md"
        }

    return res


def add_cond(condition: list, type):
    res = []
    if (condition != []):
        for i in range(0, len(condition)):
            res.append({
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
                                        "text": f"◆ {condition[i]}",
                                        "size": "md",
                                        "margin": "md",
                                        "color": "#606060FF",
                                        "weight": "bold",
                                        "align": "start",
                                        "offsetStart": "lg",
                                        "adjustMode": "shrink-to-fit"
                                    }
                                ],
                                "width": "70%"
                            },
                            {
                                "type": "filler",
                                "flex": 60
                            },
                            {

                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "X",
                                        "align": "center",
                                        "size": "md",
                                        "color": "#FF0000FF",
                                        "offsetBottom": "0px"
                                    }
                                ],
                                "action": {
                                    "type": "message",
                                    "label": "刪除",
                                    "text": f"刪除{type}-{i+1}"
                                },
                                "width": "6%",
                                "alignItems": "center",
                                "height": "80%",
                                "offsetEnd": "xl"
                            },

                        ],
                        "paddingAll": "sm",
                        "margin": "md"
                    }
                ],
                "paddingTop": "sm"
            })
    else:
        res.append({
            "type": "box",
            "layout": "horizontal",
            "contents": []
        })
    return res


def add_result(num_of_result, current_page, total_page):
    res = []
    if (num_of_result > 0):
        res = [{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                    {
                        "type": "text",
                        "text": "【查詢結果】",
                        "size": "xl",
                        "weight": "bold",
                        "style": "normal",
                        "align": "start",
                        "gravity": "center",
                        "color": "#FFFFFF"
                    },
                {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": f"共有{num_of_result}筆資料",
                                "align": "center",
                                "color": "#FFFFFF",
                                "weight": "bold",
                                "size": "lg"
                            }
                        ]
                    }
            ]
        },
            {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": f"目前頁數 : {current_page}/{total_page}",
                    "align": "center",
                    "adjustMode": "shrink-to-fit",
                    "color": "#727272FF",
                    "weight": "bold"
                }
            ]
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
        ]
    elif (num_of_result == 0):
        res = [{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                    {
                        "type": "text",
                        "text": "【查詢結果】",
                        "size": "xl",
                        "weight": "bold",
                        "style": "normal",
                        "align": "start",
                        "gravity": "center",
                        "color": "#FFFFFF"
                    },
                {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                                {
                                    "type": "text",
                                    "text": "查無資料",
                                    "align": "center",
                                    "color": "#FFFFFF",
                                    "weight": "bold",
                                    "size": "lg",
                                    "offsetTop": "xs"
                                }
                        ]
                        }
            ]
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
        }]
    return res
