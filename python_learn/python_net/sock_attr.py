"""
    套接字属性介绍
"""
from socket import *

s = socket()
# 设置socket 端口可以立即重用
# setsockopt 修改,丰富原有套接字功能
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1 or True)

s.bind(('127.0.0.1', 8989))
s.listen(5)
c, addr = s.accept()
print('地址类型', s.family)
print('套接字类型', s.type)
print('绑定地址', s.getsockname())
print('文件描述符', s.fileno())

# 链接套接字调用 结果 其实就是 addr
print('连接端地址', c.getpeername())
# 修改丰富原有套接字功能
