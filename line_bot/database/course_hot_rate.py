# 計算每堂課的熱度。

import pymysql
import math
from api import API
import global_variable as gv
# op_man 開課人數
# act_man 選課登記人數(登記人數)
# final_man 上課人數(選課人數)

class course_hot_rate() :
    def compute( year_term ) :       
        connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
        cursor = connect_db.cursor()
        
        sql = "delete from ranked_course"
        cursor.execute(sql)
        connect_db.commit()
        
        score_list = []
        rank_list = []
        op_man_list = []
        op_code = []
        teacher_cname = []
        
        sql = "SELECT * FROM op_class"
        cursor.execute(sql)
        data_now = cursor.fetchall()
        attri = cursor.description
        attr = []
        for a in attri :
            attr.append(a[0])
        
        res = API.get_op_class(year_term)
        data_old = res['dataList']
        otpair_old = []
        for d in data_old :
            otpair_old.append( [d['op_code'],d['teacher_cname']] )

        data = []
        for d in data_now :
            if [d[attr.index('op_code')],d[attr.index('teacher_cname')]] in otpair_old :
                data.append( data_old[otpair_old.index( [d[attr.index('op_code')],d[attr.index('teacher_cname')]] )] )
            else :
                op_code.append( d[attr.index('op_code')] )
                teacher_cname.append( d[attr.index('teacher_cname')] )
                rank_list.append( 0.0 )

        for d in data :
            op_code.append( d['op_code'] )
            teacher_cname.append( d['teacher_cname'] )
        for i in range( len(data) ) :   # 將開課人數、登記人數和選課人數提出，存在 score_list
            score_list.append( [data[i]['op_man'],data[i]['act_man'],data[i]['final_man']] )
        for i in range( len(score_list) ) :     # 做加權、將結果存為 rank，開課人數為 0 的資料存成 None
            if score_list[i][0] > 0 :
                if score_list[i][2]/score_list[i][0] >= 0.95 :
                    if score_list[i][1] > 0 :
                        rank_list.append( 1+math.log(score_list[i][1],1000) )
                    else :
                        rank_list.append(1)
                else :
                    if score_list[i][1] > 0 :
                        rank_list.append( (score_list[i][2]/score_list[i][0])*(1+math.log(score_list[i][1],1000)) )
                    else :
                        rank_list.append( score_list[i][2]/score_list[i][0] )
                    
            else :
                rank_list.append( 0 )
        for i in range( len(rank_list) ) :
            sql = "INSERT INTO ranked_course (op_code, teacher_cname, rank_score) VALUES (%s, %s, %s)"
            value = (op_code[i], teacher_cname[i], str(rank_list[i]))
            print(value)
            cursor.execute(sql, value)
            connect_db.commit()
        #提交修改
        # connect_db.commit()
if __name__ == "__main__":
    course_hot_rate.compute(1121) # 課程推薦度 資料庫更新 ( sql-ranked_course )
