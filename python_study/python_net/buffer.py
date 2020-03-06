"""
    buffer 文件读写缓冲机制
    缓冲刷新条件：1缓冲区满
    2。行缓冲换行时候刷新
    3。程序运行结束，文件close
    4。调用flush（）函数
"""
# 1 表示行缓冲 每次换行以后都会刷新
f = open('day02.txt.txt', 'w',1)

while True:
    date = input('>>')
    if not date:
        break
    f.write(date + '\n')
    # 刷新
    f.flush()
f.close()
