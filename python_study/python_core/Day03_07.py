"""
    练习定义 MyRange类，实现下列功能
"""
# for item in range(10):
#     print(item)


class Myrange:
    def __init__(self, stop_value):
        self.__stop_value = stop_value

    def __iter__(self):
        return MyRangeItertor(self.__stop_value)


class MyRangeItertor:
    def __init__(self, end_value):
        self.__end_value = end_value
        self.__index = 0

    def __next__(self):
        if self.__index == self.__end_value:
            raise StopIteration
        temp = self.__index
        self.__index += 1
        return temp


for item in Myrange(10):
    print(item)
