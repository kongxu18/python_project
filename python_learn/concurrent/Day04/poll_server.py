"""
    io多路复用
    poll 可以检测的数量比 select（1024） 更多，达到上万
    思路： 建立fileno --》io对象字典用于io查找
"""
import os
from socket import *
from select import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)
# 创建poll 对象
p = poll()

# 建立查找字典，通过io 的fileno 找到io对象
# 始终跟 register 的io 保持一致
fdmap = {s.fileno(): s}
# 关注 s
p.register(s, POLLIN | POLLERR)
# 监控io发生
while True:
    events = p.poll()
    # 第一个是 fileno 第二个数是 events 时间：读 写 错误等
    print(events)
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('connect from ', addr)
            # 关注客户端连接套接字
            p.register(c, POLLIN | POLLERR)
            fdmap[c.fileno()] = c
        elif event & POLLIN:  # 判断是否为 POLLIN 就绪
            # 不单单有s 还有c
            try:
                data = fdmap[fd].recv(1024).decode()
            except ConnectionResetError as e:
                print(e)
                continue
            if not data:
                print('接收的空的')
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data)
            fdmap[fd].send(b'OK')
