"""
    with 语句打开文件
"""
with open('day02.txt.txt','w+') as f:
    date = f.read()
    print(date)
# with 语句结束 f 对象自动被销毁

