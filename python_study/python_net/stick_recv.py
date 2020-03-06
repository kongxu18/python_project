"""
 tcp 粘包 客户端发送快，服务端接收慢产生粘包
 收发 先发送到网络缓冲区
"""
from socket import *
from time import sleep

sockfd = socket()
sockfd.bind('0,0,0,0', 8888)
