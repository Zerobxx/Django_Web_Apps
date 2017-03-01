#coding=utf-8
#将Excel里面的内容导入sqlite3数据库

import xlrd
import sqlite3

book = xlrd.open_workbook(u'目标表格.xlsx')
sheet = book.sheets()[0]

try:
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # 创建插入SQL语句
    query = 'INSERT INTO EventLog_inventory (name, distributor, manufacturer, model, target_device, parameters, SN, arrivaldate, num, storage_place, memo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    for r in range(1, sheet.nrows):
        name = sheet.cell(r, 0).value
        distributor = sheet.cell(r, 1).value
        manufacturer = sheet.cell(r, 2).value
        model = sheet.cell(r, 3).value
        target_device = sheet.cell(r, 4).value
        parameters = sheet.cell(r, 5).value
        SN = sheet.cell(r, 6).value
        arrivaldate = sheet.cell(r, 7).value
        num = sheet.cell(r, 8).value
        storage_place = sheet.cell(r, 9).value
        memo = sheet.cell(r, 10).value

        values = (
        name, distributor, manufacturer, model, target_device, parameters, SN, arrivaldate, num, storage_place, memo)

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



