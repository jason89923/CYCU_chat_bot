import hashlib
import imgkit
from bs4 import BeautifulSoup
import copy
from cryptography.fernet import Fernet

with open("cls_schedule.html") as fp:
    SOUP_TEMPLATE = BeautifulSoup(fp, "html.parser")


def change_schedule(soup: BeautifulSoup, sid, yearterm, weekday, time, name, room):
    div = soup.find("div")
    new_content = f"{sid} - {yearterm}學年期 功課表"
    div.string.replace_with(new_content)
    table = soup.find("table")
    cell = table.find_all("tr")[time].find_all("td")[weekday]
    br = soup.new_tag('br')
    font = soup.new_tag('font', color=666666)
    font.append(room)
    cell.clear()
    cell.append(name)
    cell.append(br)
    cell.append(font)
    return soup


def saveimage(sid, year_trem, course_list):
    options = {
        'width': 2200,
        'height': 3400,
        'quality': 30
    }

    soup = copy.copy(SOUP_TEMPLATE)
    for i in course_list:
        soup = change_schedule(soup, sid, year_trem, *i)
    imgkit.from_string(soup.prettify(), f'static/{hashlib_id(sid)}.jpg', options=options)


def hashlib_id(std_id: str):
    # 原始數據
    data = std_id.encode()
    # 創建 SHA-512 加密對象
    hash_object = hashlib.sha512()
    # 更新加密對象的數據
    hash_object.update(data)
    # 獲取加密後的結果（以十六進位字符串表示）
    hash_str = hash_object.hexdigest()
    return (hash_str)


if __name__ == '__main__':
    print(hashlib_id('10811245'))
