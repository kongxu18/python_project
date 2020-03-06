"""
向数据库插入200w条数据
"""
import pymysql

con = pymysql.connect('localhost', 'root', '333333', 'country',
                      charset='utf8')
# 获取游标
cur = con.cursor()
# 插入数据
data_list = []
for x in range(2000000):
    name = 'Tom_%s' % (x)
    data_list.append(name)

ins = "insert into students(name) values (%s)"
# 减少通信数据库次数，先统计数据，再插入数据库，这个方法不是仅仅通信一次
cur.executemany(ins, data_list)
try:
    con.commit()
except Exception as e:
    con.rollback()
cur.close()
con.close()