"""
    网络聊天室服务端
    socket upd & fork
"""
from socket import *
import os, sys

"""
    全局变量：很多地方，模块都要使用
        有一定的固定含义
"""
# 服务器地址
ADDR = ('0.0.0.0', 8888)
# 用户
user = {}


def do_login(s, name, address):
    """
    登录
    :param s:
    :param name:
    :param address:
    :return:
    """
    if name in user or '管理员' in name:
        s.sendto('该用户存在'.encode(), address)
        return
        # 可以进入聊天室
    s.sendto(b'OK', address)
    msg = '\n欢迎"%s"进入聊天室' % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    # 将新用户插入字典
    user[name] = address
    # print(user)


def do_chat(s, name, text):
    """
    聊天
    :return:
    """
    msg = '\n%s : %s' % (name, text)
    for i in user:
        if i != name:
            # print(i, '--', name)
            s.sendto(msg.encode(), user[i])


def do_quit(s, name):
    """
    退出
    :param s:
    :param name:
    :return:
    """
    msg = '\n%s 退出聊天室(服务端)' % name
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b'EXIT', user[i])
    # 删除用户
    del user[name]


def do_request(s):
    """
     处理请求
    :param s:
    :return:
    """
    while True:
        data, addr = s.recvfrom(1024)
        # 拆分请求
        tmp = data.decode().split(' ')
        # 根据不同请求类型执行不同事情
        if tmp[0] == 'L':
            # 执行登陆检测
            do_login(s, tmp[1], addr)
        elif tmp[0] == 'C':
            text = ' '.join(tmp[2:])
            do_chat(s, tmp[1], text)
        elif tmp[0] == 'Q':
            do_quit(s, tmp[1])


def main():
    """
    搭建网络
    :return:
    """
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    # 子进程的user 为自己的内存内始终是空，将消息发送给服务器自己
    if pid == 0:
        while True:
            msg = input('管理员消息：')
            msg = 'C 管理员' + msg
            s.sendto(msg.encode(), ADDR)
    elif pid>0:
        # 请求处理函数 父进程
        do_request(s)


if __name__ == '__main__':
    main()
