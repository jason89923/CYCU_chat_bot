from pprint import pprint
import pymysql
import global_variable as gv

# 改用 function : temp_info
# 存取資料形式 : [ 分數, 課程代碼, 學分數, 通過學年期 ]


class miss():

    def info(std_id, std_dept):
        db = gv.mongo_client.line_bot
        std_info = db['std_course_info']
        data_all = std_info.find_one({'stmd3_id': std_id})
        data_list = data_all['st_score']['dataList']
        dept_list = {
            '應用數學系': '應數系',
            '物理學系物理組': '物理系',
            '物理學系光電與材料科學組': '物理系',
            '化學系化學組': '化學系',
            '化學系材料化學組': '化學系',
            '心理學系': '心理系',
            '生物科技學系': '生科系',
            '奈米學位學程': '奈米學位學程',
            '工業與系統工程學系工程組': '工業系',
            '工業與系統工程學系管理組': '工業系',
            '電子工程學系': '電子系',
            '資訊工程學系': '資訊系',
            '電機工程學系': '電機系',
            '電機資訊學院人工智慧應用學士學位學程': '人工智慧學士學程',
            '電機資訊學院智慧運算與大數據學士班': '智慧運算大數據學士班',
            '電機資訊學院學士班': '電資學院學士班',
            '中原威大工程雙學士': '中原威大工程雙學士',
            '智慧運算大數據碩士': '智慧運算大數據碩士',
            '化學工程學系綠能製程組': '化工系',
            '化學工程學系生化工程組': '化工系',
            '化學工程學系材料工程組': '化工系',
            '土木工程學系': '土木系',
            '機械工程學系': '機械系',
            '生物醫學工程學系': '醫工系',
            '環境工程學系': '環工系',
            '企業管理學系服務業管理組': '企管系',
            '企業管理學系高科技業管理組': '企管系',
            '企業管理學系工商管理組': '企管系',
            '國際經營與貿易學系': '國貿系',
            '會計學系': '會計系',
            '資訊管理學系': '資管系',
            '財務金融學系': '財金系',
            '國際商學學士學程': '國際商學學士學程',
            '中原天普商學雙學士': '中原天普商學雙學士',
            '巨量碩士學程': '巨量碩士學程',
            '國際商碩': '國際商碩',
            '商學博': '商學博',
            '建築學系': '建築系',
            '商業設計學系商業設計組': '商設系',
            '商業設計學系產品設計組': '商設系',
            '室內設計學系': '室設系',
            '地景建築學系': '地景建築學系',
            '設計學院設計學士原住民專班': '設計學士原住民專班',
            '文創設計碩': '文創設計碩',
            '設計博': '設計博',
            '特殊教育學系': '特教系',
            '應用外國語文學系': '應外系',
            '應用華語文學系': '應華系',
            '師培中心': '師培中心',
            '人文與教育學院學士學位學程': '人育學士學程',
            '外籍不分系': '外籍不分系',
            '音樂產業碩士': '音樂產業碩士',
            '宗研所': '宗研所',
            '教研所': '教研所',
            '財經法律學系': '財法系'
        }
        dept = ''
        if std_dept != None:
            dept = dept_list[std_dept]

        must_course = {
            '基礎必修通識': {
                '天類': {},
                '人類': {
                    '公民': {
                        '全球化大議題': '未修習',
                        '台灣政治與民主': '未修習',
                        '法律與現代生活': '未修習',
                        '生活社會學': '未修習',
                        '當代人權議題與挑戰': '未修習',
                        '經濟學的世界': '未修習'
                    },
                    '歷史': {
                        '區域文明史': '未修習',
                        '文化思想史': '未修習',
                    }
                },
                '物類': {},
                '我類': {}
            },
            '延伸選修通識': {
                '天學': {},
                '人學': {},
                '我學': {},
                '物學': {}
            },
            '基本知能': {},
            '其他選修': {},
            '學系必修': {},
            '自由選修': {},
            '學系選修': {}
        }
        for data in data_list:
            try:
                try:
                    if data['curs_nm_c_s_a'] == '':
                        raise RuntimeError
                    cls = str(data['curs_nm_c_s_a']).replace('「跨」', '').replace('「就」', '').replace('「微」', '').replace('(英)', '').replace('「輔」', '').replace('「雙」', '')
                    if data['p_kind_name'] in must_course.keys():
                        must_course[data['p_kind_name']][cls] = False
                        must_course[data['p_kind_name']][cls] = '正在修習' if data['pass_yearterm'] != '' else False
                        must_course[data['p_kind_name']][cls] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                    elif data['p_kind_name'] in must_course['延伸選修通識'].keys():
                        must_course['延伸選修通識'][data['p_kind_name']][cls] = False
                        must_course['延伸選修通識'][data['p_kind_name']][cls] = '正在修習' if data['pass_yearterm'] != '' else False
                        must_course['延伸選修通識'][data['p_kind_name']][cls] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                    elif data['p_kind_name'] in must_course['基礎必修通識'].keys():
                        if cls in must_course['基礎必修通識']['人類']['歷史'].keys():
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls] = False
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls] = '正在修習' if data['pass_yearterm'] != '' else False
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                        elif cls in must_course['基礎必修通識']['人類']['公民'].keys():
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls] = False
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls] = '正在修習' if data['pass_yearterm'] != '' else False
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                        else:
                            must_course['基礎必修通識'][data['p_kind_name']][cls] = False
                            must_course['基礎必修通識'][data['p_kind_name']][cls] = '正在修習' if data['pass_yearterm'] != '' else False
                            must_course['基礎必修通識'][data['p_kind_name']][cls] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                except:
                    cls = str(data['curs_nm_c_s_m']).replace('「跨」', '').replace('「就」', '').replace('「微」', '').replace('(英)', '').replace('「輔」', '').replace('「雙」', '')
                    if 'pass_yearterm' in data.keys():
                        continue
                    if data['p_kind_name'] in must_course.keys():
                        must_course[data['p_kind_name']][cls] = False
                        must_course[data['p_kind_name']][cls] = '正在修習' if data['pass_yearterm'] != '' else False
                        must_course[data['p_kind_name']][cls] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                    elif data['p_kind_name'] in must_course['延伸選修通識'].keys():
                        must_course['延伸選修通識'][data['p_kind_name']][cls] = False
                        must_course['延伸選修通識'][data['p_kind_name']][cls] = '正在修習' if data['pass_yearterm'] != '' else False
                        must_course['延伸選修通識'][data['p_kind_name']][cls] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                    elif data['p_kind_name'] in must_course['基礎必修通識'].keys():
                        if cls in must_course['基礎必修通識']['人類']['歷史'].keys():
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls] = False
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls] = '正在修習' if data['pass_yearterm'] != '' else False
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                        elif cls in must_course['基礎必修通識']['人類']['公民'].keys():
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls] = False
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls] = '正在修習' if data['pass_yearterm'] != '' else False
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                        else:
                            must_course['基礎必修通識'][data['p_kind_name']][cls] = False
                            must_course['基礎必修通識'][data['p_kind_name']][cls] = '正在修習' if data['pass_yearterm'] != '' else False
                            must_course['基礎必修通識'][data['p_kind_name']][cls] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
            except:
                pass
                # print('本學期修課:', data['curs_nm_c_s_a'])
        # pprint(must_course)

        return must_course, dept

    def search_course(op_type, class_name, department, op_stdy, authority_name, search_class, year_term):
        connect_db = pymysql.connect(host=gv.SQL.host, port=gv.SQL.port, user=gv.SQL.user, passwd=gv.SQL.passwd, charset=gv.SQL.charset, db=gv.SQL.db)
        cursor = connect_db.cursor()
        to_return = []
        type_cond = ''
        cname_cond = ''
        dept_cond = ''
        stdy_cond = ''
        auth_cond = ''
        search_cond = ''
        sql = f"SELECT act_man,curs_nm_c_s,o.op_code,o.teacher_cname,dept_abvi_c,curs_lang,op_credit,op_man,op_stdy,op_type,op_time_1,cls_name_1,op_time_2,cls_name_2,op_time_3,cls_name_3,memo1,cross_name,year_term,r.rank_score FROM op_class o join ranked_course r on r.op_code=o.op_code and r.teacher_cname=o.teacher_cname WHERE year_term={year_term} AND dept_abvi_c not like %s AND dept_abvi_c not like %s"

        params = []
        params.append('%碩%')
        params.append('%博%')
        if len(department) != 0:
            dept_cond = 'admin_dept_name=%s'
            params.append(department)
            sql += " AND (" + dept_cond + ")"

        if len(op_type) != 0:
            type_cond = []
            for t in op_type:
                type_cond.append('op_type=%s')
                params.append(t)
            sql += " AND (" + ' OR '.join(type_cond) + ")"

        if len(class_name) != 0:
            cname_cond = []
            for n in class_name:
                cname_cond.append('curs_nm_c_s!=%s')
                params.append(n)
            sql += " AND (" + ' AND '.join(cname_cond) + ")"

        if len(search_class) != 0:
            search_cond = []
            for s in search_class:
                search_cond.append('curs_nm_c_s=%s')
                params.append(s)
            sql += " AND (" + ' OR '.join(search_cond) + ")"

        if len(authority_name) != 0:
            auth_cond = []
            for a in authority_name:
                auth_cond.append('authority_name=%s')
                params.append(a)
            sql += " AND (" + ' OR '.join(auth_cond) + ")"

        if len(op_stdy) != 0:
            stdy_cond = 'op_stdy=%s'
            params.append(op_stdy)
            sql += " AND (" + stdy_cond + ")"

        sql += ' and r.rank_score!=0 order by r.rank_score desc'
        cursor.execute(sql, params)
        result_set = cursor.fetchall()
        attributes = cursor.description
        for row in result_set:
            class_dict = {}
            for i in range(len(attributes)):
                class_dict[attributes[i][0]] = row[i]
            to_return.append(class_dict)
        print(sql, params)
        cursor.close()
        connect_db.close()
        return to_return

    def ge_list(std_id, std_dept, year_term):
        must_course, department = miss.info(std_id, std_dept)
        search_class = []
        department = ''
        op_type = []
        class_name = []
        for i in must_course['基礎必修通識']['天類']:
            if must_course['基礎必修通識']['天類'][i] == False:
                search_class.append(i)

        for i in must_course['基礎必修通識']['人類']:
            for j in must_course['基礎必修通識']['人類'][i]:
                try:
                    if (any(must_course['基礎必修通識']['人類'][i].values())):
                        continue
                except:
                    continue
                if must_course['基礎必修通識']['人類'][i][j] == False:
                    search_class.append(j)

        for i in must_course['基礎必修通識']['物類']:
            if must_course['基礎必修通識']['物類'][i] == False:
                search_class.append(i)

        for i in must_course['基礎必修通識']['我類']:
            if must_course['基礎必修通識']['我類'][i] == False:
                search_class.append(i)
        op_stdy = ''
        auth_cond = ''
        stdy_cond = ''
        if search_class == []:
            return [], ''
        text = ''
        return miss.search_course(op_type, class_name, department, stdy_cond, auth_cond, search_class, year_term), text

    def ge_xtend(std_id, std_dept, year_term):
        must_course, department = miss.info(std_id, std_dept)
        search_class = []
        department = ''
        op_type = []
        class_name = []
        ge_xtend_num = len(must_course['延伸選修通識']['人學']) + len(must_course['延伸選修通識']['物學']) + len(must_course['延伸選修通識']['天學']) + len(must_course['延伸選修通識']['我學'])
        if ge_xtend_num >= 14:
            return [], ''
        has_ge_xtend = 0
        if 2 * ge_xtend_num < 14:
            if len(must_course['延伸選修通識']['人學']) < 1 or len(must_course['延伸選修通識']['物學']) < 1 or len(must_course['延伸選修通識']['天學']) < 1 or len(must_course['延伸選修通識']['我學']) < 1:
                print(f'還差{14-2*ge_xtend_num}學分')
                if len(must_course['延伸選修通識']['天學']) < 1:
                    print('還須修至少一門天學的課')
                    has_ge_xtend += 1
                    op_type.append('天')
                if len(must_course['延伸選修通識']['人學']) < 1:
                    print('還須修至少一門人學的課')
                    op_type.append('人')
                    has_ge_xtend += 1
                if len(must_course['延伸選修通識']['物學']) < 1:
                    print('還須修至少一門物學的課')
                    op_type.append('物')
                    has_ge_xtend += 1
                if len(must_course['延伸選修通識']['我學']) < 1:
                    print('還須修至少一門我學的課')
                    op_type.append('我')
                    has_ge_xtend += 1
            else:
                print(f'還差{14-2*ge_xtend_num}學分，各領域已達最低門檻了')
        if 7 - ge_xtend_num > has_ge_xtend:
            op_type = ['天', '人', '物', '我']
            print('推薦你', op_type, '的課程')
        class_name.extend(must_course['延伸選修通識']['人學'])
        class_name.extend(must_course['延伸選修通識']['天學'])
        class_name.extend(must_course['延伸選修通識']['物學'])
        class_name.extend(must_course['延伸選修通識']['我學'])
        op_stdy = '選修'
        auth_cond = ''
        stdy_cond = ''
        if len(op_type) == 0:
            return [], ''
        text = ''
        return miss.search_course(op_type, class_name, department, stdy_cond, auth_cond, search_class, year_term), text

    def dept_must(std_id, std_dept, year_term):
        must_course, department = miss.info(std_id, std_dept)
        op_type = ['一般']
        stdy_cond = '必修'
        class_name = []
        search_class = []
        for i in must_course['學系必修']:
            if must_course['學系必修'][i] == False:
                search_class.append(i)
        auth_cond = ''
        if search_class == []:
            return [], ''
        text = ''
        return miss.search_course(op_type, class_name, department, stdy_cond, auth_cond, search_class, year_term), text

    def dept_choose(std_id, std_dept, year_term):
        must_course, department = miss.info(std_id, std_dept)
        op_type = ['一般']
        search_class = []
        stdy_cond = '選修'
        class_name = []
        class_name.extend(must_course['學系選修'])
        auth_cond = ''
        text = ''
        return miss.search_course(op_type, class_name, department, stdy_cond, auth_cond, search_class, year_term), text

    def knowledgh(std_id, std_dept, year_term):
        must_course, department = miss.info(std_id, std_dept)
        op_type = []
        department = ''
        auth_cond = ''
        stdy_cond = ''
        search_class = []
        class_name = []
        pprint(must_course['基本知能'])
        for i in must_course['基本知能']:
            if not must_course['基本知能'][i]:
                print(i)
                search_class.append(i)
        if search_class == []:
            return [], ''
        text = ''
        return miss.search_course(op_type, class_name, department, stdy_cond, auth_cond, search_class, year_term), text

    def recommend(std_id, std_dept, func, year_term):
        func_map = {
            '學系必修': miss.dept_must,
            '學系選修': miss.dept_choose,
            '基本知能': miss.knowledgh,
            '延伸選修通識': miss.ge_xtend,
            '基礎必修通識': miss.ge_list
            # 學系選修|學系必修|基本知能|延伸選修通識|基礎必修通識
        }

        return func_map[func](std_id, std_dept, year_term)

    def test(std_id):
        client = gv.mongo_client
        db = client.line_bot
        std_info = db['std_course_info']
        data_all = std_info.find_one({'stmd3_id': std_id})
        data_list = data_all['st_score']['dataList']
        must_course = {
            '基礎必修通識': {
                '天類': {},
                '人類': {
                    '公民': {
                        '全球化大議題': [False],
                        '台灣政治與民主': [False],
                        '法律與現代生活': [False],
                        '生活社會學': [False],
                        '當代人權議題與挑戰': [False],
                        '經濟學的世界': [False]
                    },
                    '歷史': {
                        '區域文明史': False,
                        '文化思想史': False,
                    }
                },
                '物類': {},
                '我類': {}
            },
            '延伸選修通識': {
                '天學': {},
                '人學': {},
                '我學': {},
                '物學': {}
            },
            '基本知能': {},
            '其他選修': {},
            '學系必修': {},
            '自由選修': {},
            '學系選修': {}
        }

        def process_course(data, course_type, cls, must_course):
            if course_type in must_course.keys():
                must_course[course_type][cls] = False
                must_course[course_type][cls] = '正在修習' if data.get('pass_yearterm', '') != '' else False
                must_course[course_type][cls] = data.get('score_fnal', False)

        def update_must_course(data, must_course):
            replacements = ['「跨」', '「就」', '「微」', '(英)', '「輔」', '「雙」']
            for key in ['curs_nm_c_s_a', 'curs_nm_c_s_m']:
                if key in data and data[key] != '':
                    cls = data[key]
                    for r in replacements:
                        cls = cls.replace(r, '')
                    cls = str(cls)

                    for course_type in [data['p_kind_name'], '延伸選修通識', '基礎必修通識']:
                        if course_type in ['基礎必修通識']:
                            for sub_type in ['人類', '歷史', '公民']:
                                if cls in must_course[course_type][sub_type].keys():
                                    process_course(data, must_course[course_type][sub_type][cls], cls, must_course)
                        else:
                            process_course(data, course_type, cls, must_course)

        for data in data_list:
            try:
                update_must_course(data, must_course)
            except:
                pass
        return must_course

    def temp_info(std_id):
        client = gv.mongo_client
        db = client.line_bot
        std_info = db['std_course_info']
        data_all = std_info.find_one({'stmd3_id': std_id})
        data_list = data_all['st_score']['dataList']
        must_course = {
            '基礎必修通識': {
                '天類': {},
                '人類': {
                    '公民': {
                        '全球化大議題': [False],
                        '台灣政治與民主': [False],
                        '法律與現代生活': [False],
                        '生活社會學': [False],
                        '當代人權議題與挑戰': [False],
                        '經濟學的世界': [False]
                    },
                    '歷史': {
                        '區域文明史': [False],
                        '文化思想史': [False],
                    }
                },
                '物類': {},
                '我類': {}
            },
            '延伸選修通識': {
                '天學': {},
                '人學': {},
                '我學': {},
                '物學': {}
            },
            '基本知能': {},
            '其他選修': {},
            '學系必修': {},
            '自由選修': {},
            '學系選修': {}
        }
        for data in data_list:
            try:
                try:
                    if data['curs_nm_c_s_a'] == '':
                        raise RuntimeError
                    cls = str(data['curs_nm_c_s_a']).replace('「跨」', '').replace('「就」', '').replace('「微」', '').replace('(英)', '').replace('「輔」', '').replace('「雙」', '')
                    if data['p_kind_name'] in must_course.keys():
                        must_course[data['p_kind_name']][cls] = []
                        must_course[data['p_kind_name']][cls].append(False)
                        must_course[data['p_kind_name']][cls][0] = '正在修習' if data['pass_yearterm'] != '' else False
                        must_course[data['p_kind_name']][cls][0] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                        must_course[data['p_kind_name']][cls].append(data['op_code_a']) if 'op_code_a' in data and data['op_code_a'] != None else must_course[data['p_kind_name']][cls].append('None')
                        must_course[data['p_kind_name']][cls].append(data['op_credit_a']) if 'op_credit_a' in data and data['op_credit_a'] != None else must_course[data['p_kind_name']][cls].append('None')
                        must_course[data['p_kind_name']][cls].append(data['pass_yearterm'].replace('#', '')) if 'pass_yearterm' in data and data['pass_yearterm'] != None else must_course[data['p_kind_name']][cls].append('None')

                    elif data['p_kind_name'] in must_course['延伸選修通識'].keys():
                        must_course['延伸選修通識'][data['p_kind_name']][cls] = []
                        must_course['延伸選修通識'][data['p_kind_name']][cls].append(False)
                        must_course['延伸選修通識'][data['p_kind_name']][cls][0] = '正在修習' if data['pass_yearterm'] != '' else False
                        must_course['延伸選修通識'][data['p_kind_name']][cls][0] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                        must_course['延伸選修通識'][data['p_kind_name']][cls].append(data['op_code_a']) if 'op_code_a' in data and data['op_code_a'] != None else must_course['延伸選修通識'][data['p_kind_name']][cls].append('None')
                        must_course['延伸選修通識'][data['p_kind_name']][cls].append(data['op_credit_a']) if 'op_credit_a' in data and data['op_credit_a'] != None else must_course['延伸選修通識'][data['p_kind_name']][cls].append('None')
                        must_course['延伸選修通識'][data['p_kind_name']][cls].append(data['pass_yearterm'].replace('#', '')) if 'pass_yearterm' in data and data['pass_yearterm'] != None else must_course['延伸選修通識'][data['p_kind_name']][cls].append('None')

                    elif data['p_kind_name'] in must_course['基礎必修通識'].keys():
                        if cls in must_course['基礎必修通識']['人類']['歷史'].keys():
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls] = []
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append(False)
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls][0] = '正在修習' if data['pass_yearterm'] != '' else False
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls][0] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append(data['op_code_a']) if 'op_code_a' in data and data['op_code_a'] != None else must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append('None')
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append(data['op_credit_a']) if 'op_credit_a' in data and data['op_credit_a'] != None else must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append('None')
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append(data['pass_yearterm'].replace('#', '')) if 'pass_yearterm' in data and data['pass_yearterm'] != None else must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append('None')
                        elif cls in must_course['基礎必修通識']['人類']['公民'].keys():
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls] = []
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append(False)
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls][0] = '正在修習' if data['pass_yearterm'] != '' else False
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls][0] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append(data['op_code_a']) if 'op_code_a' in data and data['op_code_a'] != None else must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append('None')
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append(data['op_credit_a']) if 'op_credit_a' in data and data['op_credit_a'] != None else must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append('None')
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append(data['pass_yearterm'].replace('#', '')) if 'pass_yearterm' in data and data['pass_yearterm'] != None else must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append('None')
                        else:
                            must_course['基礎必修通識'][data['p_kind_name']][cls] = []
                            must_course['基礎必修通識'][data['p_kind_name']][cls].append(False)
                            must_course['基礎必修通識'][data['p_kind_name']][cls][0] = '正在修習' if data['pass_yearterm'] != '' else False
                            must_course['基礎必修通識'][data['p_kind_name']][cls][0] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                            must_course['基礎必修通識'][data['p_kind_name']][cls].append(data['op_code_a']) if 'op_code_a' in data and data['op_code_a'] != None else must_course['基礎必修通識'][data['p_kind_name']][cls].append('None')
                            must_course['基礎必修通識'][data['p_kind_name']][cls].append(data['op_credit_a']) if 'op_credit_a' in data and data['op_credit_a'] != None else must_course['基礎必修通識'][data['p_kind_name']][cls].append('None')
                            must_course['基礎必修通識'][data['p_kind_name']][cls].append(data['pass_yearterm'].replace('#', '')) if 'pass_yearterm' in data and data['pass_yearterm'] != None else must_course['基礎必修通識'][data['p_kind_name']][cls].append('None')
                except:
                    cls = str(data['curs_nm_c_s_m']).replace('「跨」', '').replace('「就」', '').replace('「微」', '').replace('(英)', '').replace('「輔」', '').replace('「雙」', '')
                    if 'pass_yearterm' in data.keys():
                        continue
                    if data['p_kind_name'] in must_course.keys():
                        must_course[data['p_kind_name']][cls] = []
                        must_course[data['p_kind_name']][cls].append(False)
                        must_course[data['p_kind_name']][cls][0] = '正在修習' if data['pass_yearterm'] != '' else False
                        must_course[data['p_kind_name']][cls][0] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                        must_course[data['p_kind_name']][cls].append(data['op_code_a']) if 'op_code_a' in data and data['op_code_a'] != None else must_course[data['p_kind_name']][cls].append('None')
                        must_course[data['p_kind_name']][cls].append(data['op_credit_a']) if 'op_credit_a' in data and data['op_credit_a'] != None else must_course[data['p_kind_name']][cls].append('None')
                        must_course[data['p_kind_name']][cls].append(data['pass_yearterm'].replace('#', '')) if 'pass_yearterm' in data and data['pass_yearterm'] != None else must_course[data['p_kind_name']][cls].append('None')
                    elif data['p_kind_name'] in must_course['延伸選修通識'].keys():
                        must_course['延伸選修通識'][data['p_kind_name']][cls] = []
                        must_course['延伸選修通識'][data['p_kind_name']][cls].append(False)
                        must_course['延伸選修通識'][data['p_kind_name']][cls][0] = '正在修習' if data['pass_yearterm'] != '' else False
                        must_course['延伸選修通識'][data['p_kind_name']][cls][0] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                        must_course['延伸選修通識'][data['p_kind_name']][cls].append(data['op_code_a']) if 'op_code_a' in data and data['op_code_a'] != None else must_course['延伸選修通識'][data['p_kind_name']][cls].append('None')
                        must_course['延伸選修通識'][data['p_kind_name']][cls].append(data['op_credit_a']) if 'op_credit_a' in data and data['op_credit_a'] != None else must_course['延伸選修通識'][data['p_kind_name']][cls].append('None')
                        must_course['延伸選修通識'][data['p_kind_name']][cls].append(data['pass_yearterm'].replace('#', '')) if 'pass_yearterm' in data and data['pass_yearterm'] != None else must_course['延伸選修通識'][data['p_kind_name']][cls].append('None')
                    elif data['p_kind_name'] in must_course['基礎必修通識'].keys():
                        if cls in must_course['基礎必修通識']['人類']['歷史'].keys():
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls] = []
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append(False)
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls][0] = '正在修習' if data['pass_yearterm'] != '' else False
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls][0] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append(data['op_code_a']) if 'op_code_a' in data and data['op_code_a'] != None else must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append('None')
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append(data['op_credit_a']) if 'op_credit_a' in data and data['op_credit_a'] != None else must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append('None')
                            must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append(data['pass_yearterm'].replace('#', '')) if 'pass_yearterm' in data and data['pass_yearterm'] != None else must_course['基礎必修通識'][data['p_kind_name']]['歷史'][cls].append('None')
                        elif cls in must_course['基礎必修通識']['人類']['公民'].keys():
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls] = []
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append(False)
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls][0] = '正在修習' if data['pass_yearterm'] != '' else False
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls][0] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append(data['op_code_a']) if 'op_code_a' in data and data['op_code_a'] != None else must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append('None')
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append(data['op_credit_a']) if 'op_credit_a' in data and data['op_credit_a'] != None else must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append('None')
                            must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append(data['pass_yearterm'].replace('#', '')) if 'pass_yearterm' in data and data['pass_yearterm'] != None else must_course['基礎必修通識'][data['p_kind_name']]['公民'][cls].append('None')
                        else:
                            must_course['基礎必修通識'][data['p_kind_name']][cls] = []
                            must_course['基礎必修通識'][data['p_kind_name']][cls].append(False)
                            must_course['基礎必修通識'][data['p_kind_name']][cls][0] = '正在修習' if data['pass_yearterm'] != '' else False
                            must_course['基礎必修通識'][data['p_kind_name']][cls][0] = (data['score_fnal']) if 'score_fnal' in data else '正在修習'
                            must_course['基礎必修通識'][data['p_kind_name']][cls].append(data['op_code_a']) if 'op_code_a' in data and data['op_code_a'] != None else must_course['基礎必修通識'][data['p_kind_name']][cls].append('None')
                            must_course['基礎必修通識'][data['p_kind_name']][cls].append(data['op_credit_a']) if 'op_credit_a' in data and data['op_credit_a'] != None else must_course['基礎必修通識'][data['p_kind_name']][cls].append('None')
                            must_course['基礎必修通識'][data['p_kind_name']][cls].append(data['pass_yearterm'].replace('#', '')) if 'pass_yearterm' in data and data['pass_yearterm'] != None else must_course['基礎必修通識'][data['p_kind_name']][cls].append('None')
            except:
                pass

        return (must_course)


if __name__ == '__main__':
    pprint(miss.temp_info('11228227'))
    # pprint(miss.info('11245243','資訊工程學系'))
    # pprint(miss.test('11145212'))
    # name = []
    # (miss.recommend('11045243','資訊工程學系','延伸選修通識',1121))
    # for i in (miss.recommend('11127211','資訊工程學系','通識基礎必修')):
    #     if i['']
    # pprint(miss.info('10811245','資訊工程學系'))
