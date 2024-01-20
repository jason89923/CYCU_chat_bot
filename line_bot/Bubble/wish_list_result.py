def wish_list_result_card(search_res):
    body_content = make_body_content(search_res)
    res = {
        "type": "bubble",
        "size": "mega",
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
                             "text": check_text(search_res['op_stdy']),
                             "align": "start",
                             "size": "sm",
                             "color": "#000000",
                             "weight": "bold"
                         },
                         {
                             "type": "text",
                             "text": f"{search_res['op_credit']}學分",
                             "align": "start",
                             "size": "sm",
                             "color": "#000000",
                             "weight": "bold"
                         }
                     ],
                    "width": "20%",
                    "justifyContent": "center",
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": check_text(search_res['curs_nm_c_s']),
                            "size": "md",
                            "align": "center",
                            "weight": "bold",
                            "wrap": True
                        }
                    ],
                    "alignItems": "center",
                    "justifyContent": "center"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "♥",
                            "size": "xxl",
                            "weight": "bold",
                            "color": "#FF2929A0",
                            "action": {
                                "type": "message",
                                "label": "移除追蹤清單",
                                "text": f"移除追蹤清單-{check_text(search_res['op_code'])}"
                            }
                        }
                    ],
                    "width": "25%",
                    "height": "70px",
                    "alignItems": "center",
                    "justifyContent": "center"
                }
            ],
            "paddingAll": "lg",
            "background": {
                "type": "linearGradient",
                "angle": "135deg",
                "startColor": "#B96A9CAB",
                "endColor": "#FF98987F",
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
                                                        "text": "👉 授課老師 :",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "adjustMode": "shrink-to-fit"
                                                    }
                                                ],
                                                "width": "50%"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": check_text(search_res['teacher_cname']),
                                                        "size": "sm",
                                                        "wrap": True,
                                                        "align": "end"
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
                                                        "text": "👉 開課系級 :",
                                                        "size": "md",
                                                        "adjustMode": "shrink-to-fit",
                                                        "weight": "bold"
                                                    }
                                                ],
                                                "width": "50%"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": check_text(search_res['dept_abvi_c']),
                                                        "size": "sm",
                                                        "adjustMode": "shrink-to-fit",
                                                        "align": "end"
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
                                                        "text": "👉 課程代碼 :",
                                                        "size": "md",
                                                        "adjustMode": "shrink-to-fit",
                                                        "weight": "bold"
                                                    }
                                                ],
                                                "width": "50%"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": check_text(search_res['op_code']),
                                                        "size": "sm",
                                                        "adjustMode": "shrink-to-fit",
                                                        "align": "end"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ],
                        "paddingBottom": "md"
                    },
                {
                        "type": "separator",
                        "color": "#000000"
                        },
                {
                        "type": "box",
                        "layout": "vertical",
                        "contents": body_content,
                        "paddingTop": "lg"
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
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "📙",
                                        "size": "xxl",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "上課用書",
                                        "align": "center",
                                        "color": "#FFFFFF",
                                        "weight": "bold"
                                    }
                                ]
                            }
                        ],
                        "borderWidth": "bold",
                        "alignItems": "center",
                        "backgroundColor": "#5C8A84FF",
                        "borderColor": "#3B3B3B89",
                        "cornerRadius": "20px",
                        "action": {
                            "type": "message",
                            "label": "查詢上課用書",
                            "text": f"查詢{search_res['op_code']}之上課用書"
                        }
                    },
                {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "paddingAll": "none",
                        "width": "5%"
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
                                        "text": "📜",
                                        "size": "xxl",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "課程大綱",
                                        "align": "center",
                                        "color": "#FFFFFF",
                                        "weight": "bold"

                                    }
                                ]
                            }
                        ],
                        "borderWidth": "bold",
                        "backgroundColor": "#5C8A84FF",
                        "borderColor": "#3B3B3B89",
                        "cornerRadius": "20px",
                        "alignItems": "center",
                        "action": {
                            "type": "uri",
                            "label": "課程大綱",
                            "uri": f"https://cmap.cycu.edu.tw:8443/Syllabus/CoursePreview.html?yearTerm={str(search_res['year_term'] or '無')}&opCode={str(search_res['op_code'] or '無')}"
                        }

                        }
            ],
            "alignItems": "center"
        }
    }

    return res


def make_body_content(search_res):
    content = []

    if search_res['op_time_1'] is not None:
        content += [{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "✦ 上課時間1 :",
                                "size": "md",
                                "weight": "bold",
                                "adjustMode": "shrink-to-fit"
                            }
                        ],
                        "width": "50%"
                    },
                {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": check_text(search_res['op_time_1']),
                                "size": "sm",
                                "wrap": True,
                                "align": "end"
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
                                "text": "✦ 上課地點1 :",
                                "size": "md",
                                "weight": "bold",
                                "adjustMode": "shrink-to-fit"
                            }
                        ],
                        "width": "50%"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": check_text(search_res['cls_name_1']),
                                "size": "sm",
                                "wrap": True,
                                "align": "end"
                            }
                        ]
                    }
                ]
        }]

    if search_res['op_time_2'] is not None:
        content += [{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "✦ 上課時間2 :",
                                "size": "md",
                                "weight": "bold",
                                "adjustMode": "shrink-to-fit"
                            }
                        ],
                        "width": "50%"
                    },
                {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": check_text(search_res['op_time_2']),
                                "size": "sm",
                                "wrap": True,
                                "align": "end"
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
                                "text": "✦ 上課地點2 :",
                                "size": "md",
                                "weight": "bold",
                                "adjustMode": "shrink-to-fit"
                            }
                        ],
                        "width": "50%"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": check_text(search_res['cls_name_2']),
                                "size": "sm",
                                "wrap": True,
                                "align": "end"
                            }
                        ]
                    }
                ]
        }]
    if search_res['op_time_3'] is not None:
        content += [{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "✦ 上課時間3 :",
                                "size": "md",
                                "weight": "bold",
                                "adjustMode": "shrink-to-fit"
                            }
                        ],
                        "width": "50%"
                    },
                {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": check_text(search_res['op_time_3']),
                                "size": "sm",
                                "wrap": True,
                                "align": "end"
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
                                "text": "✦ 上課地點3 :",
                                "size": "md",
                                "weight": "bold",
                                "adjustMode": "shrink-to-fit"
                            }
                        ],
                        "width": "50%"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": check_text(search_res['cls_name_3']),
                                "size": "sm",
                                "wrap": True,
                                "align": "end"
                            }
                        ]
                    }
                ]
        }]
    res = [{
        "type": "box",
        "layout": "vertical",
        "contents": content
    }]

    return res


def check_text(text: str):
    if (text == None):
        return '無'
    if (len(text.replace(' ', '').replace('\n', '').replace('\t', '')) == 0):
        return '無'
    return text


def check_follow(text: str):
    if (check_text(text) != '無'):
        return text + '-'
    return ''
