import pymysql
import global_variable as gv

def delete_one(std_id, op_code) :
    connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
    cursor = connect_db.cursor()
    sql = f"DELETE FROM wishlist WHERE std_id = '{std_id}' AND op_code = '{op_code}'"
    try :
        cursor.execute(sql)
        connect_db.commit()
        return True
    except :
        return False