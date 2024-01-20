from pprint import pprint
from formal_api import API
import global_variable as gv


def std_course_info(std_id):
    client = gv.mongo_client
    db = client.line_bot
    std_info = db['std_course_info']
    res = std_info.find_one({'stmd3_id': std_id})
    if res == None:
        info_json = API.get_std_course_info(std_id)
        std_info.insert_one(info_json['total']['this_year_st']['dataList'][0])
    else:
        return res
    return info_json['total']['this_year_st']['dataList'][0]


def insert_all_std_course_info(std_id):
    client = gv.mongo_client
    db = client.line_bot
    std_info = db['std_course_info']
    res = std_info.find_one({'stmd3_id': std_id})
    if res == None:
        response = API.get_std_course_info(std_id)
        course_list = []
        course_list.extend(response['this_st']['st_score']['dataList'])
        for page in range(int(response['this_st']['st_score']['pageCount']) - 1):
            response = API.get_std_course_info(std_id, str(page + 2))
            course_list.extend(response['this_st']['st_score']['dataList'])
        response['this_st']['st_score']['dataList'] = course_list
        std_info.insert_one(response['this_st'])
    else:
        return res
    return response['this_st']

if __name__ == '__main__':
    # student_info = insert_all_std_course_info('11282626')
    # student_dept = student_info['dep_name']
    # for course in student_info['st_score']['dataList']:
    #     if 'pass_yearterm' in course.keys() and course['pass_yearterm'] == '1112':
    #         print(course['curs_nm_c_s_a'])

    pprint(insert_all_std_course_info('11145132'))
    # print(insert_all_std_course_info('10813201')['dep_name'])
    # print(insert_all_std_course_info('10813323')['dep_name'])
