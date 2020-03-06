"""
    io encode decode
    所有字符串 都能转 字节串
    并不是所有字节串 都能 转字符串
"""
# 将字符串转为字节串
s = '你好'.encode()

print(s)
# 字节串 转为 字符串
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode())