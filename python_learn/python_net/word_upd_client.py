"""
    字典查询客户端
"""
from socket import *

ADDR = ('127.0.0.1', 8888)

# 创建套接字 数据报套接字 有消息边界不会产出粘包
sockfd = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('word：')
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("from server:", msg.decode())

sockfd.close()