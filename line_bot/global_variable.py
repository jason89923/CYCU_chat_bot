import redis
import pymongo
import os
from flask import g


DEBUG = False

if not DEBUG:
    os.chdir('/home/tliw1/Cycu_line_bot/line_bot')
else:
    os.chdir('/home/tliw1/Cycu_line_bot/test_env/line_bot')

BUBBLE_MAX_PAGE = 7

URL = 'https://mycycuchatbot.cycu.edu.tw/static/'


SESSION = redis.Redis(host='localhost', port=6379, decode_responses=True, db=0)
SEARCH_COURSE_CACHE = redis.Redis(host='localhost', port=6379, decode_responses=True, db=1)
LB_INFO_CACHE = redis.Redis(host='localhost', port=6379, decode_responses=True, db=3)
TEST_ACCOUNT_LOGIN_TOKEN = redis.Redis(host='localhost', port=6379, decode_responses=True, db=4)
RECOMMEND_COURSE_CACHE = redis.Redis(host='localhost', port=6379, decode_responses=True, db=5)
WATER_BALLOONS_DATABASE = redis.Redis(host='localhost', port=6379, decode_responses=True, db=6)
CURRICULUM_CACHE = redis.Redis(host='localhost', port=6379, decode_responses=True, db=7)
USER_LOG = redis.Redis(host='localhost', port=6379, decode_responses=True, db=8)
CONFIG_CACHE = redis.Redis(host='localhost', port=6379, decode_responses=True, db=9)

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/', connect=False)


DEVELOPER = set(("U85b23a2893e94d12a16721ade9118bab", "U3bc27358b993bb49beee34b806e9cd30", "U5b112051297e315e373c20c915b35b6a",
                 "U42a4dc0982f07dd0faf15d276f6c3cbc", "Udba17413f48608a625b11071768b25c7", "Ua1bfb915560b199fd52b0adedb67f3cd",
                 "Ufeb6589bdc774053207297b7d95a6efe", "U77fb4ef7eb211ad2b3340fabf8d4cd16", 'U0923f6786c1d047fe86da388594d468c', 'U5e3f79547f994cd6c7e3ba38cd52628d', 'Ufd3404c2374e9f1fb628ec971ea82b72'))

LB_INFO_MAP = {'館藏地': 'location', '索書號': 'id', '條碼': 'barcode', '狀態': 'status', '其他訊息': 'other'}

if not DEBUG:
    class LINE_CHANNEL:
        ACCESS_TOKEN = "PMdxIMriqWiizuvp4Df/jBu4jGEKwAtS9jF1e2z/D7cqzpKT9vS4E5B5Dmac+FsNa4OOcMUBbwgHjEerwL71J+pGtPxCkqO8oMc1UoGK5qRNbz1RKWJQLMGDsMmuW3ZVkTVIaYyqKs9BR0zB29YQ8AdB04t89/1O/w1cDnyilFU="
        SECRET = "04a54f10063b11caa83065332658b93a"
else:    
    class LINE_CHANNEL:
        ACCESS_TOKEN = "rjBEjE1Rppe62jbqn46zNqeT2HclMEKPxBdn9dbU0ckz0sLqeA5g3n8tURmZCayJC8nepD7Wv1P9VlV8tGGTV9cWzd5kFk7ZQEBnN3oJn54oc8QVOLTToVvXZRSmCoqX+7bSVQittbUrMj0btimeaAdB04t89/1O/w1cDnyilFU="
        SECRET = "c4559e0688ca895b5926e6a361c73c01"


class API:
    APP_TOKEN = "1e25ca860a43f170c8becd871471b67c258162dcbd6cab"
    APP_ID = "2005"
    KEY = "28d6b2910db112051edd610d758eac8f"
    Formal_URL = "https://mobile.cycu.edu.tw/api/"
    Formal_LOGIN = "https://itouch.cycu.edu.tw"
    TEST_LOGIN = "https://beta.cycu.edu.tw"
    URL = "https://beta.cycu.edu.tw/api/"


class SQL:
    host = "127.0.0.1"
    port = 3306
    user = "root"
    passwd = "Cycust4062057"
    charset = "utf8"
    db = "myCYCU"


DEPARTMENT = {
    "理學院": {
        "url": f"{URL}dept/tab1.png",
        "dept_names": [
            "應數系",
            "物理系",
            "化學系",
            "心理系",
            "生科系",
            "奈米學位學程"
        ],
        "dept_names_abbr": [
            "應數系",
            "物理系",
            "化學系",
            "心理系",
            "生科系",
            "奈米學程"
        ]
    },
    "工學院": {
        "url": f"{URL}dept/tab2.png",
        "dept_names": [
            "化工系",
            "土木系",
            "機械系",
            "醫工系",
            "環工系"
        ],
        "dept_names_abbr": [
            "化工系",
            "土木系",
            "機械系",
            "醫工系",
            "環工系"
        ]
    },
    "商學院": {
        "url": f"{URL}dept/tab3.png",
        "dept_names": [
            "企管系",
            "國貿系",
            "會計系",
            "資管系",
            "財金系",
            "國際商學學士學程",
            "中原天普商學雙學士"
        ],
        "dept_names_abbr": [
            "企管系",
            "國貿系",
            "會計系",
            "資管系",
            "財金系",
            "國際商學",
            "天普雙學士"
        ]
    },
    "設計學院": {
        "url": f"{URL}dept/tab4.png",
        "dept_names": [
            "建築系",
            "商設系",
            "室設系",
            "地景建築學系",
            "設計學士原住民專班"
        ],
        "dept_names_abbr": [
            "建築系",
            "商設系",
            "室設系",
            "地景系",
            "原住民專班"
        ]
    },
    "人文與教育學院": {
        "url": f"{URL}dept/tab5.png",
        "dept_names": [
            "特教系",
            "應外系",
            "應華系",
            "師培中心",
            "產業人才中心",
            "人育學士學程",
            "外籍不分系"
        ],
        "dept_names_abbr": [
            "特教系",
            "應外系",
            "應華系",
            "師培中心",
            "人才中心",
            "人育學程",
            "外籍不分系"
        ]
    },
    "法學院": {
        "url": f"{URL}dept/tab6.png",
        "dept_names": [
            "財法系"
        ],
        "dept_names_abbr": [
            "財法系"
        ]
    },
    "電機資訊學院": {
        "url": f"{URL}dept/tab7.png",
        "dept_names": [
            "工業系",
            "電子系",
            "資訊系",
            "電機系",
            "人工智慧學士學程",
            "電資學院學士班",
            "中原威大工程雙學士",
            "智慧運算大數據學士班"
        ],
        "dept_names_abbr": [
            "工業系",
            "電子系",
            "資訊系",
            "電機系",
            "AI學程",
            "電資學士班",
            "威大雙學士",
            "智慧運算"
        ]
    }
}
