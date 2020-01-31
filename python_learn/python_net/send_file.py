"""
 客户端发送文件
"""
from socket import *

s = socket()
s.connect(('127.0.0.1', 8888))

# 读取文件，循环发送
f = open('timg.jpeg', 'rb')
while True:
    date = f.read(1024)
    if not date:
        break
    s.send(date)
f.close()
s.close()
