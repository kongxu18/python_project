"""
    udp 套接字服务端流程
"""
from socket import *

# 创建套接字 数据报套接字 有消息边界不会产出粘包
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ('127.0.0.1', 8888)
sockfd.bind(server_addr)

# 循环收发消息
while True:
    # 不会产生粘包 超过的就会发生丢失
    data, addr = sockfd.recvfrom(5)
    print('收到：', data.decode())
    sockfd.sendto(b'>>', addr)

# 关闭套接字
sortfd.close()