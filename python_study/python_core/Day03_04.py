"""
    迭代器
"""


class Skill:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return str(self.id)


class SkillIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        """
        返回下一个数据
        :return:
        """
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        """
        重写
        创建一个迭代器对象
        :return:
        """
        return SkillIterator(self.__skills)


manager = SkillManager()
manager.add_skill(Skill(1))
manager.add_skill(Skill(2))
manager.add_skill(Skill(3))

"""
    查看类中 有几个对象
"""
iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
#
# for item in manager:
#     print(item)
