"""
封装实例变量
"""


class Wife:
    def __init__(self, name, age, hp):
        self.name = name
        # 对象点变量名 这是不再是对实例变量操作，而是类变量 被拦截了
        self.age = age
        self.hp = hp

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    # 属性 property对象拦截对age类变量读写操作
    age = property(get_age, set_age)

    def set_hp(self, value):
        self.__hp = value

    # 这样就是不能读写
    hp = property(None, set_hp)


w01 = Wife('a', 12, 1)
print(w01.__dict__)
w01.age = 30
print(w01.age)
print(w01.__dict__)
# print(w01.hp)
"""
最终的版本  使用属性property 封装
"""


class Wife02:
    def __init__(self, name, age, hp):
        self.name = name
        # 对象点变量名 这是不再是对实例变量操作，而是类变量 被拦截了
        self.age = age
        self.hp = hp

    @property
    def age(self):
        return self.__age+200

    @age.setter
    def age(self, value):
        self.__age = value

w02=Wife02('amm',12,100)

w02.age=300
print(w02.age)
print(w02.__dict__)