list02 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(id(list02))
list02.remove(6)
# 不能这么删除，列表的索引会改变

print(id(list02))
result = ''
# 每次循环形成新的字符串 替换变量引用，不建议这么做
for item in range(10):
    result += str(item)
    print(id(result))
'''
所以字符串拼接 join
'''

# 字符串拼接 内存没有变啊？？


a = ''
print(id(a))
a += 'a'
print(id(a))
