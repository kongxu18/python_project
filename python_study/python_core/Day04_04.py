"""
生成器练习
"""


class SkillDate:
    def __init__(self, id, name, atk, duration):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration

    def __str__(self):
        return str(self.name)


list_skill = [
    SkillDate(101, 'a', 5, 10),
    SkillDate(102, 'b', 8, 1),
    SkillDate(103, 'c', 10, 5),
    SkillDate(104, 'd', 7, 2),
]


# 获取攻击比例大于6的所有技能
def fun01():
    for item in list_skill:
        if item.atk > 6:
            yield item


result = fun01()
for item in fun01():
    print(item)

