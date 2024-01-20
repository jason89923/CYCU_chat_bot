from pprint import pprint
import pymysql
import global_variable as gv
# note : this is the official version of searching classes.
# different from the original version ( search_class.py ), the database which saves the op_time is changed from 70 up schema to 7 schema 


class search_class():

    def search(op_time, teacher_cname, op_type, class_name, department, year_term):        
        connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
        cursor = connect_db.cursor()
        to_return = []
        time_cond = ''
        tname_cond = ''
        type_cond = ''
        cname_cond = ''
        depart_cond = ''
        sql = f"SELECT * FROM op_class o JOIN class_time c ON o.op_code=c.op_code WHERE o.year_term={year_term}"
        params = []


        if len(op_time) != 0:
            for time in op_time:
                c_date, c_time = search_class.separate_time(time)
                for i in range(3) :
                    if i != 0 or time != op_time[0] :
                        time_cond += ' OR '
                    time_cond += '(c.time_' + str(i+1) + "_Day_of_Week=%s AND ("
                    params.append(c_date)
                    for c in range(len(c_time)) :
                        if c != 0 :
                            time_cond += ' OR '
                        time_cond += "c.time_"+ str(i+1) +"_time like %s"
                        params.append('%' + c_time[c] + '%')
                    time_cond += '))'
            sql += " AND (" + time_cond + ")"
            
            
        if len(teacher_cname) != 0:
            tname_cond = []
            for n in teacher_cname:
                tname_cond.append('o.teacher_cname LIKE %s')
                params.append('%' + n + '%')
            sql += " AND (" + ' OR '.join(tname_cond) + ")"

        if len(class_name) != 0:
            cname_cond = []
            for n in class_name:
                Blur_str = ''
                for n_char in n:
                    Blur_str += '%' + n_char
                Blur_str += '%'
                cname_cond.append('o.curs_nm_c_s LIKE %s')
                params.append(Blur_str)
            sql += " AND (" + ' OR '.join(cname_cond) + ")"

        if len(op_type) != 0:
            type_cond = []
            for t in op_type:
                type_cond.append('o.op_type = %s')
                params.append(t)
            sql += " AND (" + ' OR '.join(type_cond) + ")"

        if len(department) != 0:
            depart_cond = []
            for d in department:
                depart_cond.append('o.admin_dept_name = %s')
                params.append(d)
            sql += " AND (" + ' OR '.join(depart_cond) + ")"
        cursor.execute(sql, params)
        result_set = cursor.fetchall()
        attributes = cursor.description
        for row in result_set:
            class_dict = {}
            for i in range(len(attributes)):
                class_dict[attributes[i][0]] = row[i]
            to_return.append(class_dict)
        cursor.close()
        connect_db.close()
        return to_return
        
    def separate_time(op_time):
        day_to_eng = {
            '1': 'mon',
            '2': 'tue',
            '3': 'wed',
            '4': 'thu',
            '5': 'fri',
            '6': 'sat',
            '7': 'sun'
        }
        date = op_time[0]
        time = op_time[2:]
        date = day_to_eng[date]
        return date, time

    def batch_search(year_term, time, teacher, type, name, department, **kwargs):
        return search_class.search(time, teacher, type, name, department, year_term)


if __name__ == '__main__':
    # start = time.time()
    result = (search_class.batch_search(1112,['1-12'], [], [], [],['資訊系','應數系']))
    pprint(result)

