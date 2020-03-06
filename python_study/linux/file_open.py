"""
    file open
"""
try:
    # fd =open('a.py','r')
    fd = open('a.py', 'w')  # 只写方式打开
    # 追加方式
    fc = open('a.py', 'a')
    # 二进制打开 普通文本都可以使用
    fd = open('a.py', 'rb')
    print(fd)
except Exception as e:
    print(e)
