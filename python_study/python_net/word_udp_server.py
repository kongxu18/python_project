"""
    udp 字典服务端
"""
# 服务端提供逻辑和数据处理
from socket import *


def find_word(word):
    # 默认只读打开
    f = open('dict.txt')
    for line in f:
        w = line.split(' ')[0]
        if w > word:
            f.close()
            return '没有找到'
        elif w == word:
            f.close()
            return line
    else:
        f.close()
        return '没有找到这个单词'


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
    result = find_word(data.decode())
    sockfd.sendto(b'>>%s' % result.encode(), addr)

# 关闭套接字
sortfd.close()
