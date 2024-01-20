import pymysql
try:
    from course_hot_rate import course_hot_rate
    from api import API
except:
    from database.course_hot_rate import course_hot_rate
    from database.api import API
from pprint import pprint
import global_variable as gv

# 更新資料前請先執行 delete_op_class.py


class op_class():

    data = ''
    keys = ''
    t_data = ''
    t_keys = ''
    op_code_list = []

    def separate(op_time, op_code, num_of_time):
        day_to_eng = {
            '1': 'mon',
            '2': 'tue',
            '3': 'wed',
            '4': 'thu',
            '5': 'fri',
            '6': 'sat',
            '7': 'sun'
        }
        if op_time != None:
            date = op_time[0]
            time = op_time[2:]
            op_class.t_data += ',\'' + (day_to_eng[date] if date in day_to_eng else 'NA') + '\', \'' + time + '\''
            op_class.t_keys += ', time_' + num_of_time + '_Day_of_Week, time_' + num_of_time + '_time'

    def get_op_cls(year_term):

        data_list = []
        key_list = []
        t_data_list = []
        t_key_list = []
        res = API.get_op_class(year_term)
        for i in range(len(res['dataList'])):
            op_class.data = ''
            op_class.keys = ''
            has_time = False
            key = res['dataList'][i].keys()
            key = sorted(key)
            for j in key:
                op_class.t_keys = ''
                op_class.t_data = ''
                if ('op_time' in j):
                    has_time = True
                    if res['dataList'][i]['op_code'] not in op_class.op_code_list:
                        op_class.op_code_list.append(res['dataList'][i]['op_code'])
                        t_data_list.append('\'' + res['dataList'][i]['op_code'] + '\'')
                        t_key_list.append('op_code')
                    op_class.separate(str(res['dataList'][i][j]), res['dataList'][i]['op_code'], str(j[len(j) - 1]))
                    if op_class.t_data not in t_data_list[op_class.op_code_list.index(res['dataList'][i]['op_code'])]:
                        t_data_list[op_class.op_code_list.index(res['dataList'][i]['op_code'])] += op_class.t_data
                        t_key_list[op_class.op_code_list.index(res['dataList'][i]['op_code'])] += op_class.t_keys
                if (res['dataList'][i][j]) != '':
                    op_class.keys += j
                    if (j != 'tch_t_count' and j != 'op_t_count' and j != 'op_credit' and j != 'op_man' and j != 'act_man' and j != 'final_man'):
                        op_class.data += "'" + str(res['dataList'][i][j]).replace("'", "\\'") + "'"
                    else:
                        op_class.data += str(res['dataList'][i][j])
                if j != key[len(key) - 1]:
                    op_class.data += ','
                    op_class.keys += ','
            if (not has_time):
                op_class.op_code_list.append(res['dataList'][i]['op_code'])
                t_data_list.append('\'' + res['dataList'][i]['op_code'] + '\'')
                t_key_list.append('op_code')
            data_list.append(op_class.data)
            key_list.append(op_class.keys)
        return data_list, key_list, t_data_list, t_key_list

    def insert_to_sql(year_term):

        connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
        cursor = connect_db.cursor()
        op_class.delete_op_class()
        value, schema, t_value, t_schema = op_class.get_op_cls(year_term)
        error_num = 0
        for i in range(len(value)):
            # SQL語法
            sql = "INSERT INTO op_class(" + schema[i] + ") VALUES (" + value[i] + ")"

            try:
                cursor.execute(sql)
                # 提交修改
                connect_db.commit()
                # print('success')
            except:
                # 發生錯誤時停止執行SQL
                connect_db.rollback()
                print(sql)
                print(value[i])
                print(schema[i])
                print('error')
                error_num += 1
        print("錯誤共:", error_num, "\napi共: ", len(t_value))
        for i in range(len(t_value)):
            # SQL語法
            sql = "INSERT INTO class_time(" + t_schema[i] + ") VALUES (" + t_value[i] + ")"

            try:
                cursor.execute(sql)
                # 提交修改
                connect_db.commit()
            except:
                # 發生錯誤時停止執行SQL
                connect_db.rollback()
                if t_value not in op_class.op_code_list:
                    print(sql)
                    print(t_value[i])
                    print(t_schema[i])
                    print('error')
                error_num += 1
        print("共有", len(op_class.op_code_list), "不重複的課程代碼")
        course_hot_rate.compute(year_term)
        # 關閉連線

    def delete_op_class():
        connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
        cursor = connect_db.cursor()
        sql = "DELETE FROM op_class"
        cursor.execute(sql)
        connect_db.commit()
        sql = "DELETE FROM class_time"
        cursor.execute(sql)
        connect_db.commit()


if __name__ == '__main__':
    op_class.insert_to_sql('1121')
