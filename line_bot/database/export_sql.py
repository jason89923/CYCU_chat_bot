import pymysql
from pprint import pprint
import csv
from datetime import date
import global_variable as gv

def export(your_table) :
    connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)    
    cursor = connect_db.cursor()
    sql_query = f"SELECT * FROM {your_table}"

    # 執行 SQL 查詢
    cursor = connect_db.cursor()
    cursor.execute(sql_query)
    results = cursor.fetchall()

    # CSV 檔案路徑
    csv_file = f'sql_export/{your_table}_{str(date.today().strftime("%m%d"))}.csv'

    # 寫入 CSV 檔案
    with open(csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([i[0] for i in cursor.description])  # 寫入欄位名稱
        csv_writer.writerows(results)  # 寫入資料

    # 關閉連線
    cursor.close()
    connect_db.close()

    print("資料已成功匯出為CSV檔案。")

def delete_table(your_table):

    connect_db = pymysql.connect(
        host=gv.SQL.host,
        port=gv.SQL.port,
        user=gv.SQL.user,
        passwd=gv.SQL.passwd,
        charset=gv.SQL.charset,
        db=gv.SQL.db
    )
    cursor = connect_db.cursor()
    sql = f"DELETE FROM {your_table}"

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


if __name__ == '__main__':
    export('system_feedback')
    # delete_table("line_error_message")