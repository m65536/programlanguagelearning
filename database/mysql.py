#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'password',
    'db':'tx_order',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor
    }
conn = pymysql.connect(**config)
conn.autocommit(1)
cursor = conn.cursor()

try:
    DB_NAME = 'tx_order'
    conn.select_db(DB_NAME)

    # 查询数据条目
    count = cursor.execute('SELECT * FROM tx_order limit 100')
    print 'total records:', cursor.rowcount

    results = cursor.fetchall()
    print results
    for result in results:
        # print result.u_user_id
        print result
        print result["create_user_name"]

except:
    import traceback
    traceback.print_exc()
    # 发生错误时会滚
    conn.rollback()
finally:
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    conn.close()
