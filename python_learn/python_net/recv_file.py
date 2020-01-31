"""
    将一个文件从客户端发送到服务端保存
    服务端接收文件
"""
from socket import *

s = socket()
s.bind(('127.0.0.1', 8888))
s.listen(3)

c, addr = s.accept()
print('connect from ', addr)

# 接收文件
file = open('gg.jpeg', 'wb')
while True:

    data =c.recv(1024)
    if not data:
        break
    file.write(data)
file.close()
c.close()
s.close()
