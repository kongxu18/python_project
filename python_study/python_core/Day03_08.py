"""
    生成器 generator
"""


class Myrange:
    def __init__(self, stop_value):
        self.__stop_value = stop_value

    def __iter__(self):
        """
            调用 iter 当前方法不执行 内部创建迭代器
            调用 __next__方法才执行
            执行到 yield 语句 暂时离开
            再次调用 __next__ 继续执行
            重复 3，4步骤，直至最后
        :return:
        """
        # return MyRangeItertor(self.__stop_value)
        #         0 --> 10
        number = 0
        while number < self.__stop_value:
            """
            yield 标记 
                将下列代码改为迭代器模式的代码
                生成迭代器代码的大致规则
                    1。将yield 以前的语句定义在next 方法中
                    2。将yield 后面的数据作为 next 方法返回值
                
            """
            yield number
            number += 1


# for item in Myrange(10):
#     print(item)
manager = Myrange(10)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

"""
    yield --> 生成器
"""


class MyGenertor:
    """
    生成器 = 可迭代对象 + 迭代器
    """

    def __init__(self, stop_value):
        self.stop_value = stop_value
        self.begin = 0

    def __iter__(self):
        return self

    def __next__(self):
        pass


def __iter__(stop_value):
    number = 0
    while number < stop_value:
        yield number
        number += 1


my01 = __iter__(3)
print(dir(my01))
for item in my01:
    print(item)

"""
    生成器和迭代器 关系
"""
