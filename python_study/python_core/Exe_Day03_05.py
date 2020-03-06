"""
    图形管理器记录多个图形
    迭代图形管理器对象
"""


class Graphics:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)


class GraphicsItertor:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


class DrawingManager:
    def __init__(self):
        self.__Graphics = []

    def add_graphics(self, value):
        self.__Graphics.append(Graphics(value))

    def __iter__(self):
        # return GraphicsItertor(self.__Graphics)
        """
        使用生成器
        :return:
        """
        for i in range(len(self.__Graphics)):
            yield self.__Graphics[i]


manager = DrawingManager()
manager.add_graphics(1)
manager.add_graphics(2)
manager.add_graphics(3)
# manager = []
for item in manager:
    print(item)
