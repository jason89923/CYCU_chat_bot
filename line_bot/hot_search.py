import pymysql
from pprint import pprint
from search_class import search_class
import global_variable as gv


class hot_search:
    def add_t_point(course_list: list):
        connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
        cursor = connect_db.cursor()
        course = ''
        for i in course_list:
            if i != course_list[0]:
                course += ' OR '
            course += f"op_code='{str(i['op_code'])}'"
        sql = f"UPDATE hot_result set score=score+1 where ({course});"
        try:
            cursor.execute(sql)
            # 提交修改
            connect_db.commit()
        except:
            print('error', '\n', sql)
            # 發生錯誤時停止執行SQL
            connect_db.rollback()

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
        keys = []
        for c in time:
            key = ''
            key += 'c.' + day_to_eng[date] + '_' + c
            keys.append(key)
        return keys

    def hot_course(cond, s_type):
        connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
        cursor = connect_db.cursor()
        op_time = cond['time']
        teacher_cname = cond['teacher']
        class_name = cond['name']
        op_type = cond['type']
        dept = cond['department']
        if s_type == 'teacher':
            sql_cond = "o.teacher_cname!=' '"
        elif s_type == 'name':
            sql_cond = "o.curs_nm_c_s!=' '"
        else :
            sql_cond = "o.admin_dept_name!=' '"
        time_cond = ''
        tname_cond = ''
        type_cond = ''
        cname_cond = ''
        depart_cond = ''
        if len(op_time) != 0:
            for time in op_time:
                c_date, c_time = search_class.separate_time(time)
                for i in range(3) :
                    if i != 0 or time != op_time[0] :
                        time_cond += ' OR '
                    time_cond += '(c.time_' + str(i+1) + '_Day_of_Week=\'' + c_date + '\' AND ('
                    for c in range(len(c_time)) :
                        if c != 0 :
                            time_cond += ' OR '
                        time_cond += 'c.time_' + str(i+1) + '_time like \'%' + c_time[c] + '%\''
                    time_cond += '))'
            sql_cond += " AND (" + time_cond + ")"
        if len(teacher_cname) != 0:
            for n in teacher_cname:
                if n != teacher_cname[0]:
                    tname_cond += ' OR '
                tname_cond += 'o.teacher_cname=\'' + n + '\''
            sql_cond += " AND (" + tname_cond + ")"
        if len(class_name) != 0:
            for n in class_name:
                Blur_str = ''
                if n != class_name[0]:
                    cname_cond += ' OR '
                for n_char in n:
                    Blur_str += '%' + n_char
                Blur_str += '%'
                cname_cond += 'o.curs_nm_c_s LIKE \'' + Blur_str + '\''
            sql_cond += " AND (" + cname_cond + ")"
        if len(op_type) != 0:
            for t in op_type:
                if t != op_type[0]:
                    type_cond += ' OR '
                type_cond += 'o.op_type=\'' + t + '\''
            sql_cond += " AND (" + type_cond + ")"
        if len(dept) != 0:
            for d in dept:
                if d != dept[0]:
                    depart_cond += ' OR '
                depart_cond += 'o.admin_dept_name=\'' + d + '\''
            sql_cond += " AND (" + depart_cond + ")"
        # 系級
        type_list = {
            'teacher': 'teacher_cname',
            'name': 'curs_nm_c_s',
            'department' : 'admin_dept_name'
        }
        sql = f"SELECT DISTINCT * FROM (SELECT o.admin_dept_name,o.teacher_cname,o.curs_nm_c_s,o.op_time_1,h.score FROM hot_result h JOIN op_class o ON (h.teacher_cname=o.teacher_cname)AND(h.op_code=o.op_code) JOIN class_time c ON c.op_code=o.op_code WHERE {sql_cond}) as hot_courses ORDER BY score DESC limit 10"
        if time_cond == '' and tname_cond == '' and type_cond == '' and cname_cond == '' and s_type == 'department': 
            sql = "SELECT admin_dept_name FROM hot_result GROUP BY admin_dept_name LIMIT 10"
        cursor.execute(sql)
        result_set = cursor.fetchall()
        attributes = cursor.description
        to_return = []
        for row in result_set:
            class_dict = {}
            for i in range(len(attributes)):
                class_dict[attributes[i][0]] = row[i]
            to_return.append(class_dict)
        cursor.close()
        connect_db.close()
        return to_return


if __name__ == '__main__':
    # hot_seacher.add_t_point(['AC003D','AC000A'])
    pprint(hot_search.hot_course({'type': [], 'time': ['1-12'], 'teacher': [], 'name': [], 'department' : []}, 'teacher'))
