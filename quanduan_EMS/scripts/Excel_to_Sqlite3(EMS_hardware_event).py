#coding=utf-8
#将Excel里面的内容导入sqlite3数据库

import xlrd
import sqlite3

book = xlrd.open_workbook(u'目标表格.xls')
sheet = book.sheets()[0]

try:
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # 创建插入SQL语句
    query = 'INSERT INTO EventLog_hardware_event (malfunction_date, hostname, addr, manufacturer, func_type, model, sn, event_phenomenon, reason_judge, event_level, malfunction_part, part_model, solution, restore_time, IDC, location, batch, distributor, update_time, memo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    for r in range(1, sheet.nrows):
        malfunction_date = sheet.cell(r, 0).value
        hostname = sheet.cell(r, 1).value
        addr = sheet.cell(r, 2).value
        manufacturer = sheet.cell(r, 3).value
        func_type = sheet.cell(r, 4).value
        model = sheet.cell(r, 5).value
        sn = sheet.cell(r, 6).value
        event_phenomenon = sheet.cell(r, 7).value
        reason_judge = sheet.cell(r, 8).value
        event_level = sheet.cell(r, 9).value
        malfunction_part = sheet.cell(r, 10).value
        part_model = sheet.cell(r, 11).value
        solution = sheet.cell(r, 12).value
        restore_time = sheet.cell(r, 13).value
        IDC = sheet.cell(r, 14).value
        location = sheet.cell(r, 15).value
        batch = sheet.cell(r, 16).value
        distributor = sheet.cell(r, 17).value
        update_time = sheet.cell(r, 18).value
        memo = sheet.cell(r, 19).value

        values = (malfunction_date, hostname, addr, manufacturer, func_type, model, sn, event_phenomenon, reason_judge, event_level, malfunction_part, part_model, solution, restore_time, IDC, location, batch, distributor, update_time, memo)

        cursor.execute(query, values)

    cursor.close()

    conn.commit()

    print 'Done!'
    columns = str(sheet.ncols)
    rows = str(sheet.nrows-1)
    print 'import %s rows %s columns to sqlite3 db!' % (rows, columns)

except Exception:

    print 'DB query executed error!'

finally:

    conn.close()



