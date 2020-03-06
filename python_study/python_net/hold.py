"""
    空洞文件
"""
f=open('day02.txt.txt','wb')
f.write(b'start')
# 从结尾向后移动1k
f.seek(1024*1024,2)
f.write(b'end')
f.close()