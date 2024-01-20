import insert_op_class_official
import insert_hot_teacher
import global_variable as gv
from course_hot_rate import course_hot_rate

def update_academic_year():
    gv.CONFIG_CACHE.set('YEAR_TERM', '1122')

def update_database():
    year_term = gv.CONFIG_CACHE.get('YEAR_TERM')
    insert_op_class_official.op_class.insert_to_sql(year_term) # 開課資訊 資料庫更新 ( sql-op_class )
    insert_hot_teacher.insert(year_term) # 課程熱門查詢度 資料庫更新 ( sql-hot_course )



if __name__ == "__main__":
    update_academic_year()
    update_database()
    course_hot_rate.compute('1121') # 填入上一個學年