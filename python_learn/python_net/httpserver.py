"""
    v1.0 httpserver
    1.获取来自浏览器的请求
    2。判断如果请求内容是 / 将index 返回给客户端
    3。如果请求其他内容 返回404
"""
from socket import *


# 客户端处理
def request(connfd):
    #     获取请求，将内容提取出来
    # 判断是 / 返回index 不是返回404
    data = connfd.recv(4096).decode()
    # 防止浏览器异常退出 data 为空
    if not data:
        return
    request_line = data.split('/n')[0]
    info = request_line.split(' ')[1]
    print(info)
    if info == '/':
        with open('index.html') as f:
            res = "HTTP/1.1 200 OK\r\n"
            res += "Content-Type:text/html\r\n"
            res += "\r\n"
            res += f.read()
    else:
        res = "HTTP/1.1 404 NOT FOUND\r\n"
        res += "Content-Type:text/html\r\n"
        res += "\r\n"
        res += "<h1>Sorry</h1>"
    connfd.send(res.encode())
# 搭建tcp网络
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('0.0.0.0', 8000))
sockfd.listen(5)
while True:
    connfd, addr = sockfd.accept()
    request(connfd)
