"""
    使用udp完成客户端录入学生信息发送服务端
    struct
"""
from socket import *
import struct
# 数据格式定义
st =struct.Struct('i32sif')
s = socket(AF_INET,SOCK_DGRAM)
ADDR=('127.0.0.1',8888)
while True:
    print('---')
    id =int(input('id:'))
    name =input('name:').encode()
    age =int(input('age:'))
    score =float(input('score:'))
    # 打包数据发送
    data=st.pack(id,name,age,score)
    s.sendto(data,ADDR)