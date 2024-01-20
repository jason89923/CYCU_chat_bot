import pymysql
import global_variable as gv

class wish_list():
    def search(std_id):
        connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
        cursor = connect_db.cursor()
        sql = "SELECT * FROM wishlist w JOIN op_class o ON ( o.op_code = w.op_code AND ( CASE WHEN w.teacher_cname = 'XXXX' THEN 1 ELSE o.teacher_cname = w.teacher_cname END ) AND o.year_term = w.year_term ) where std_id = '%s'" % std_id
        cursor.execute(sql)
        result = cursor.fetchall()
        attributes = cursor.description
        to_return = []
        need_list = "curs_nm_c_s,op_code,teacher_cname,dept_abvi_c,curs_lang,op_credit,op_man,op_stdy,op_type,op_time_1,cls_name_1,op_time_2,cls_name_2,op_time_3,cls_name_3,memo1,cross_name,year_term"
        for row in result:
            class_dict = {}
            for i in range(len(attributes)):
                if (attributes[i][0] in need_list):
                    class_dict[attributes[i][0]] = row[i]
            to_return.append(class_dict)
        return to_return
    def delete_wishlist():
        connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
        cursor = connect_db.cursor()
        sql = "Delete From wishlist"
        cursor.execute(sql)
        connect_db.commit()
if __name__ == "__main__" :
    wish_list.delete_wishlist()
