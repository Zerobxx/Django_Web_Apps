#coding=utf-8
#将Excel里面的内容（合同维保信息）导入sqlite3数据库

import xlrd
import sqlite3

book = xlrd.open_workbook(u'目标表格.xlsx')
sheet = book.sheets()[0]

try:
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # 创建插入SQL语句
    query = 'INSERT INTO EventLog_constracts (constract_num, constract_name, constract_date, project_batch, contract_details, contract_first_party, contract_second_party, maintenance_level_and_time, maintenance_start_time, maintenance_end_time, whether_under_guarantee, constract_services, memo, updatetime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    for r in range(1, 18):
        constract_num = sheet.cell(r, 0).value
        constract_name = sheet.cell(r, 1).value
        if sheet.cell(r, 2).value:
            constract_date = xlrd.xldate.xldate_as_datetime(sheet.cell(r, 2).value, 0).date()
        else:
            constract_date = None
        print str(constract_date)+' constract_date'
        project_batch = sheet.cell(r, 3).value
        contract_details = sheet.cell(r, 4).value
        contract_first_party = sheet.cell(r, 5).value
        contract_second_party = sheet.cell(r, 6).value
        maintenance_level_and_time = sheet.cell(r, 7).value
        if sheet.cell(r, 8).value:
            maintenance_start_time = xlrd.xldate.xldate_as_datetime(sheet.cell(r, 8).value, 0).date()
        else:
            maintenance_start_time = None
        print maintenance_start_time
        maintenance_end_time = sheet.cell(r, 9).value
        whether_under_guarantee = sheet.cell(r, 10).value
        constract_services = sheet.cell(r, 11).value
        memo = sheet.cell(r, 12).value
        updatetime = sheet.cell(r, 13).value

        values = (constract_num, constract_name, constract_date, project_batch, contract_details, contract_first_party, contract_second_party, maintenance_level_and_time, maintenance_start_time, maintenance_end_time, whether_under_guarantee, constract_services, memo, updatetime)

        cursor.execute(query, values)

    cursor.close()

    conn.commit()

    print 'Done!'

    columns = str(sheet.ncols)
    rows = str(17)
    print 'import %s rows %s columns to sqlite3 db!' % (rows, columns)

except Exception:
    print 'DB query executed error!'

finally:

    conn.close()