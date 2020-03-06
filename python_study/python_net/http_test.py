"""
    http 请求演示过程

"""
from socket import *

# 创建套接字
s = socket()
s.bind(('0.0.0.0', 8000))
s.listen(5)

c, addr = s.accept()
print('connect from ', addr)
# 接收http请求

data = c.recv(4096)
print(data)
# 将数据组织为相应格式
response = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>hello world</h1>
"""
c.send(response.encode())
c.close()
s.close()