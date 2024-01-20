import global_variable as gv
from formal_api import API
def login_bubble(uid):
    res = {
        "type": "bubble",
        "size": "kilo",
        "hero": {
            "type": "image",
            "url": f"{gv.URL}bubble/中原選課輔導機器人.png",
            "size": "full",
            "action": {
                "type": "uri",
                "label": "action",
                "uri": f"{API.itouch_login(uid)}"
            }
        }
    }
    return res
if __name__ == '__main__':
    print(login_bubble("Uf1f7c9e7d5a2a8b2b8a8f7b4f7a8b0a2"))