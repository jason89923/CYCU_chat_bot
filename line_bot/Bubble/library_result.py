def library_card(title='未知', edition='未知', author='未知', location='未知', id='未知', status='未知', booktype='未知', **kwargs):
    res = {
        "type": "bubble",
        "size": "mega",
        "direction": "ltr",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "○",
                            "size": "xxl",
                            "offsetBottom": "sm",
                            "align": "start",
                            "gravity": "center",
                            "wrap": True,
                            "weight": "bold",
                            "color": "#53535389"
                        }
                    ],
                    "offsetBottom": "xxl",
                    "offsetEnd": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": title,
                            "size": "lg",
                            "wrap": True,
                            "align": "center",
                            "weight": "bold",
                            "color": "#494949FF"
                        }
                    ],
                    "offsetBottom": "xxl",
                    "paddingBottom": "none"
                }
            ],
            "background": {
                "type": "linearGradient",
                "angle": "135deg",
                "startColor": "#66E0B1AB" if booktype == '參考書' else "#74BEA1AA",
                "endColor": "#6676E07F" if booktype == '參考書' else "#4DCE3F72",

            },
            "paddingBottom": "lg"
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
                            "text": "📕圖書資訊",
                            "align": "start",
                            "contents": [],
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": add_info(author, edition, booktype),
                            "paddingTop": "md"
                        }
                    ],
                    "paddingBottom": "lg"
                },
                {
                    "type": "separator",
                    "color": "#000000"
                }
            ]
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
                            "text": "📖館藏狀態",
                            "align": "start",
                            "contents": [],
                            "weight": "bold",
                            "size": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": add_status(location, id, status)
                                }
                            ],
                            "paddingTop": "md",
                            "paddingStart": "xxl"
                        }
                    ],
                    "paddingBottom": "lg"
                }
            ],
            "paddingStart": "xxl"
        }
    }
    return res


def add_info(author, edition, booktype):
    if (edition != '未知'):
        res = [{
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
                                    "text": "⚉ 版次 : ",
                                    "size": "md",
                                    "weight": "bold",
                                    "adjustMode": "shrink-to-fit"
                                }
                            ],
                            "width": "40%"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": edition,
                                    "size": "sm",
                                    "wrap": True,
                                    "offsetStart": "xl",
                                    "adjustMode": "shrink-to-fit"
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
                                    "text": "⚉ 作者:",
                                    "size": "md",
                                    "weight": "bold",
                                    "adjustMode": "shrink-to-fit"
                                }
                            ],
                            "width": "40%"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": author,
                                    "size": "sm",
                                    "wrap": True,
                                    "offsetStart": "xl",
                                    "align": "start"
                                }
                            ],
                            "PaddingEnd": "xxl"
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
                                    "text": "⚉ 書本類型 :",
                                    "size": "md",
                                    "adjustMode": "shrink-to-fit",
                                    "weight": "bold"
                                }
                            ],
                            "width": "40%"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": booktype,
                                    "size": "sm",
                                    "offsetStart": "xl",
                                    "adjustMode": "shrink-to-fit"
                                }
                            ]
                        }
                    ]
                }
            ],
            "paddingStart": "xxl"
        }]
    else:
        res = [{
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
                                    "text": "⚉ 作者:",
                                    "size": "md",
                                    "weight": "bold",
                                    "adjustMode": "shrink-to-fit"
                                }
                            ],
                            "width": "40%"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": author,
                                    "size": "sm",
                                    "wrap": True,
                                    "offsetStart": "xl",
                                    "align": "start"
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
                                    "text": "⚉ 書本類型 :",
                                    "size": "md",
                                    "adjustMode": "shrink-to-fit",
                                    "weight": "bold"
                                }
                            ],
                            "width": "40%"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": booktype,
                                    "size": "sm",
                                    "offsetStart": "xl",
                                    "adjustMode": "shrink-to-fit"
                                }
                            ]
                        }
                    ]
                }
            ],
            "paddingStart": "xxl"
        }]
    return res


def add_status(location, id, status):
    if (status == '未知'):
        res = [{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "⚉ 目前狀態 :",
                            "size": "md",
                            "adjustMode": "shrink-to-fit",
                            "weight": "bold"
                        }
                    ],
                    "width": "40%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "館內無此書",
                            "size": "sm",
                            "offsetStart": "xl",
                            "adjustMode": "shrink-to-fit"
                        }
                    ]
                }
            ]
        }]
    else:
        res = [{
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "⚉ 索書號 : ",
                            "size": "md",
                            "weight": "bold",
                            "adjustMode": "shrink-to-fit"
                        }
                    ],
                    "width": "40%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "size": "sm",
                            "wrap": True,
                            "offsetStart": "xl",
                            "adjustMode": "shrink-to-fit",
                            "text": id
                        }
                    ]
                }
            ],
            "PaddingEnd": "xl"
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
                            "text": "⚉ 目前狀態 :",
                            "size": "md",
                            "adjustMode": "shrink-to-fit",
                            "weight": "bold"
                        }
                    ],
                    "width": "40%"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": status,
                            "size": "sm",
                            "offsetStart": "xl",
                            "adjustMode": "shrink-to-fit"
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
                            "text": "⚉ 館藏地 :",
                            "size": "md",
                            "weight": "bold",
                            "adjustMode": "shrink-to-fit"
                        }
                    ],
                    "width": "40%"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": location,
                            "size": "sm",
                            "wrap": True,
                            "offsetStart": "xl",
                            "adjustMode": "shrink-to-fit"
                        }
                    ],
                    "paddingEnd": "xl"
                }
            ]
        }]
    return res
