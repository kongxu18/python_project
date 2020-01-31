"""
    聊天室客户端
"""
from socket import *
import os, sys

ADDR = ('127.0.0.1', 8888)


def send_msg(s, name):
    """
    发送消息
    :param s:
    :return:
    """
    while True:
        try:
            text = input('>')
        except KeyboardInterrupt:
            text = 'quit'
        if text.strip() == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(), ADDR)
            sys.exit('退出聊天室(客户端)')
        msg = 'C %s %s' % (name, text)
        s.sendto(msg.encode(), ADDR)


def recv_msg(s):
    while True:
        try:
            data, addr = s.recvfrom(2048)
        except KeyboardInterrupt:
            sys.exit()
        # 从服务器收到EXIT退出
        if data.decode() == 'EXIT':
            sys.exit('客户端退出')
        print(data.decode(), end=' ')


def main():
    s = socket(AF_INET, SOCK_DGRAM)
    # 进入聊天室
    while True:
        name = input('name>>')
        msg = 'L ' + name
        s.sendto(msg.encode(), ADDR)
        # 接收反馈
        data, addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print('进入聊天室')
            break
        else:
            print(data.decode())
    # 已经进入聊天室
    pid = os.fork()
    if pid < 0:
        sys.exit('ERROR!')
    elif pid == 0:
        send_msg(s, name)
    else:
        recv_msg(s)


if __name__ == '__main__':
    main()
