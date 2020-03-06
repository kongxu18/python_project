"""
    每秒写入一行时间
"""
import time

f = open('log.txt', 'a+')
# 将偏移量移到开头
f.seek(0, 0)
n = 0
for line in f:
    n += 1
while True:
    n += 1
    time.sleep(1)
    s = '%d.%s\n' % (n, time.ctime())
    f.write(s)
    # 刷新
    f.flush()
