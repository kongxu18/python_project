"""
    查询字典  复制一个文档
"""
word = input('Word:')

# 默认只读打开
f = open('dict.txt')

for line in f:
    w = line.split(' ')[0]
    if w > word:
        print('没有找到')
        break
    elif w == word:
        print(line)
        break
else:
    print('没有找到这个单词')

f.close()

"""
    复制一个文件
"""
filename = input('File:')
try:
    fr = open(filename, 'rb')
except FileExistsError as e:
    print(e)
else:
    fw = open('file_copy.jpg', 'wb')
    while True:
        date = fr.read(1024)
        if not date:
            break
        fw.write(date)
    fr.close()
    fw.close()
