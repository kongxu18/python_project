"""
面向对象 第一天
"""
# 面向对象思想 随意创建类 并调用方法


"""
学生信息
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.age, self.name)


list01 = []
while True:
    name = input('name')
    if name == '':
        break
    s01 = Student(name, age=1)
    list01.append(s01)

print(list01)

for item in list01:
    item.print_info()
