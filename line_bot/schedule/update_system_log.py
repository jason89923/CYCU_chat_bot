import pymysql
import redis
import json
import global_variable as gv


def insert_log(date, uid, sid, input, state, waiting_for, is_command):
    connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
    cursor = connect_db.cursor()
    sql = "INSERT INTO system_log VALUES (%s,%s,%s,%s,%s,%s,%s)"
    value = date, uid, sid, input, state, waiting_for, is_command
    try:
        cursor.execute(sql, value)
        # 提交修改
        connect_db.commit()
        return True
    except:
        # 發生錯誤時停止執行SQL
        print('insert_log error')
        connect_db.rollback()
        return False


def insert_system_feedback(uid, sid, text):
    connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
    cursor = connect_db.cursor()
    sql = "INSERT INTO system_feedback VALUES (%s,%s,%s)"
    value = uid, sid, text
    try:
        cursor.execute(sql, value)
        # 提交修改
        connect_db.commit()
        return True
    except:
        # 發生錯誤時停止執行SQL
        print('insert_log error')
        connect_db.rollback()
        return False


def insert_line_error_message(datetime, uid, error_message):
    connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
    cursor = connect_db.cursor()
    sql = "INSERT INTO line_error_message VALUES (%s,%s,%s)"
    value = datetime, uid, error_message
    try:
        cursor.execute(sql, value)
        # 提交修改
        connect_db.commit()
        return True
    except:
        # 發生錯誤時停止執行SQL
        print('insert_log error')
        connect_db.rollback()
        return False


if __name__ == "__main__":
    USER_LOG = redis.Redis(host='localhost', port=6379, decode_responses=True, db=8)
    while USER_LOG.llen('user_log') > 0:
        result = json.loads(USER_LOG.lpop('user_log'))
        insert_log(*result)
