"""
继承 --设计
"""

"""
需求 ：老周 开车 去东北
变化：
    坐飞机
    汽车
"""

# 依赖倒置抽象 开闭原则
class Vehicle:
    """
    交通工具
    隔离子类变化，将子类的共性提取到父类中
    """
    def transport(self, str_position):
        # 父类太过于抽象写不出方法体
        pass


# 客户端代码，用交通工具
class Person:
    def __init__(self,name):
        self.name=name


    def go_to(self, vehicle, str_position):
        # 调用是交通工具的运输方法
        vehicle.transport(str_position)


class Car(Vehicle):
    def transport(self, str_position):
        print('汽车开', str_position)


class Plane(Vehicle):
    def transport(self, str_position):
        print('飞机', str_position)


p01 = Person('老章')
c01 = Car()
a01 = Plane()

p01.go_to(c01,'东北')
