import pymysql
from pprint import pprint
import global_variable as gv
from search_class import search_class
def insert(year_term) :

    connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)    
    cursor = connect_db.cursor()
    
    sql = "delete from hot_result"
    cursor.execute(sql)
    connect_db.commit()
    
    resu = search_class.search([],[],[],[],[],year_term)
    
    success_op_class = []
    fail_list = []
    for res in resu :
        sql = "INSERT INTO hot_result(op_code, teacher_cname, admin_dept_name, score) VALUES (%s, %s, %s, 0)"
        params = (res['op_code'], res['teacher_cname'], str(res['admin_dept_name'])or'')
        try:
            cursor.execute(sql,params)
            #提交修改
            connect_db.commit()
            success_op_class.append(res['op_code'])
        except:
            if res['op_code'] not in success_op_class and res['op_code'] not in fail_list:
                print('ERROR : ',params)
                fail_list.append(res['op_code'])
            #發生錯誤時停止執行SQL
            connect_db.rollback()

if __name__ == '__main__':
    insert()
    # delete_db()