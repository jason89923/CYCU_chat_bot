import pymysql
import global_variable as gv
def insert(teacher_cname, op_code, line_id, year_term):
    connect_db = pymysql.connect(
        host=gv.SQL.host,
        port=gv.SQL.port,
        user=gv.SQL.user,
        passwd=gv.SQL.passwd,
        charset=gv.SQL.charset,
        db=gv.SQL.db
    )
    cursor = connect_db.cursor()

    values = (teacher_cname, op_code, line_id)
    sql = f"INSERT INTO wishlist (teacher_cname, op_code, year_term, std_id) VALUES (%s, %s, {year_term}, %s)"

    try:
        cursor.execute(sql, values)
        connect_db.commit()
        return True
    except:
        connect_db.rollback()
        return False
    finally:
        cursor.close()
        connect_db.close()
        
def delete_wish_list():
    connect_db = pymysql.connect(
        host=gv.SQL.host,
        port=gv.SQL.port,
        user=gv.SQL.user,
        passwd=gv.SQL.passwd,
        charset=gv.SQL.charset,
        db=gv.SQL.db
    )
    
    cursor = connect_db.cursor()
    sql = f"DELETE FROM wishlist"

    try:
        cursor.execute(sql)
        connect_db.commit()
        return True
    except:
        connect_db.rollback()
        return False
    finally:
        cursor.close()
        connect_db.close()
