"""
    tcp客户端流程
"""
from socket import *

# 创建tcp套接字 默认参数就是tcp套接字
sockfd = socket()

# 绑定可以不写，客户端绑定存在风险

# 连接服务器
server_addr = ('172.0.0.1', 8888)

sockfd.connect(server_addr)
while True:
    date = input('msg>>')
    if not date :
        break
    sockfd.send(date.encode())
    date = sockfd.recv(1024)
    print('server', date.decode())

sockfd.close()
