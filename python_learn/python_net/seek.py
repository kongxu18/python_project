"""
    文件偏移量
    1.每次open 打开文件偏移量都在开头
    2。已 a 方式打开时文件偏移量在结尾
    3。读写操作共用一个文件偏移量
"""
f = open('day02.txt.txt', 'rb+')
date = f.read(5)
print('文件偏移量', f.tell())
# 操作移动偏移量 相对于末尾移动0个
f.seek(0, 2)
f.write(b'%%123')
f.close()
