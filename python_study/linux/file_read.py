"""
    file read
"""

f = open('test', 'r')

while False:
    # 读到文件结尾就返回空字符串
    date = f.read(10)
    if not date:
        break
    print('>', date)

# 读取一行内容
while False:
    date = f.readline(10)
    if not date:
        break
    print('一行内容', date)

# 读取每一行作为列表中的一项
while False:
    # 前18 个字符所在的行作为读取对象
    date = f.readlines(18)
    if not date:
        break
    print('>', date)

# f 为可迭代对象
for i in f:
    # 每次读一行
    print('>', i)
f.close()
