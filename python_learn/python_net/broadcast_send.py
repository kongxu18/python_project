"""
    udp 广播发送
    1。创建upd 套接字
    2。设置可以发送光笔
    3。循环向广播地址发送
"""
from socket import *
from time import sleep

# 广播地址
dest = ('127.0.0.1', 9999)
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

data = """
    sdaadsadjsadaj
"""
num =0
while True:
    sleep(2)
    num +=1
    data =data + str(num)
    s.sendto(data.encode(),dest)

