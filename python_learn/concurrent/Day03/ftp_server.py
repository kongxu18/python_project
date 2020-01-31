"""
    ftp 文件服务器，服务端
    多进程/线程兵法 socket
"""
from socket import *
from threading import Thread

# 全局变量
HOST = '0.0.0.0'
PORT = 8080
ADDR = (HOST, PORT)
FTP =''

# 创建类实现服务器文件处理功能
class FTPServer:
    """
    查看列表，下载，上传，退出处理
    """


# 搭建网络服务端模型
def main():
    s = socket()
    s.bind(ADDR)
    s.listen(5)


if __name__ == '__main__':
    main()
