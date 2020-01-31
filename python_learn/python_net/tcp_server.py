"""
    tcp 套接字服务端流程
"""
import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址
sockfd.bind(('127.0.0.1', 8888))
# 设置监听 代表可建立socket连接的最大个数
sockfd.listen(5)
while True:
    # 阻塞等待处理连接
    print('waiting for connect...')
    try:
        # connfd 客户端连接套接字
        connfd, addr = sockfd.accept()
        # 打印链接的客户端地址
        print('connect from ', addr)
    except KeyboardInterrupt:
        print('server exit')
        break
    except Exception as e:
        print(e)
        continue
    while True:
        # 收发消息
        # 如果客户端断开，recv不再阻塞 返回空
        date = connfd.recv(1024)
        # 如果date为空的话 客户端退出
        if not date:
            break
        print('收到', date.decode())
        # 发送字节串
        n = connfd.send(b'Thanks>>')
        print('发送%d字节' % n)
    # 关闭套接字
    connfd.close()
sockfd.close()
