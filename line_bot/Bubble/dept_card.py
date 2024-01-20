import global_variable as gv


def bubble(dept_dict):
    res = {
        "type": "bubble",
        "size": "kilo",
        "direction": "ltr",
        "body": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": dept_dict['url'],
                            "size": "sm",
                            "align": "center",
                            "gravity": "center"
                        }
                    ],
                    "width": "35%",
                    "justifyContent": "center",
                    "alignItems": "center",
                    "paddingEnd": "sm"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "borderWidth": "medium",
                    "borderColor": "#FF853460",
                    "width": "1%"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": add_dept(dept_dict['dept_names_abbr'],dept_dict['dept_names']),
                    "paddingStart": "sm",
                    "justifyContent": "center",
                    "offsetStart": "xl"
                }
            ],
            "paddingAll": "sm",

        }
    }
    return res


def add_dept(dept_list,dept_names):
    res = []
    for dept,names in zip(dept_list,dept_names):
        res.append({
            "type": "text",
            "text": f"🔗 {dept}",
            "align": "start",
            "weight": "bold",
            "size": "md",
            "margin": "lg",
            "action": {
                "type": "message",
                "label": dept,
                "text": names
            },
        })
    return res


def carousel():

    dept_dict = gv.DEPARTMENT
    dept_bubble = []
    for college in sorted(dept_dict.values(), key=lambda x: len(x['dept_names']), reverse=True):
        dept_bubble.append(bubble(college))

    res = {
        "type": "carousel",
        "contents": dept_bubble
    }
    return res
