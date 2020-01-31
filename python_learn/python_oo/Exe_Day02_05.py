"""
练习
"""


class Student:
    def __init__(self, name, age, sex, score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    def print_info(self):
        print(self.age, self.name)


list01 = [
    Student("阿呆", 23, '男', 122),
    Student("苏大强", 4, '女', 33),
    Student("三大", 3, '男', 22),
    Student("二大", 1, '女', 454)
]


# 查询苏大强 将名称与年龄返回
def search_name(tlist, tname=''):
    for item in tlist:
        if item.name == '苏大强':
            return item


# 如果没有找到 返回空 函数默认返回空 none 可以不写
stu = search_name(list01)
print(stu.name, stu.age)


# 查询所有女的
def fun02():
    return [item for item in list01 if item.sex == '女']


# a = fun02()
for item in fun02():
    item.print_info()


# 查找年龄大于20的数目
def fun03():
    count = 0
    for item in list01:
        if item.age > 20:
            count += 1
        return count


print(fun03())


# 将所有人 成绩设置为0
def fun04():
    for item in list01:
        item.score = 0


fun04()
for item in list01:
    print(item.score, item.name)


# 获取 所有学生名字
def fun05():
    return [item.name for item in list01]


print(fun05())


# 查找年龄最大的对象
def fun06():
    max_stu = list01[0]
    for i in range(1, len(list01)):
        if max_stu.age < list01[i].age:
            max_stu = list01[i]
    return max_stu


re = fun06()
re.print_info()
