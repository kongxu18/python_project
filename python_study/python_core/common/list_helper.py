"""

"""


class ListHelper:
    @staticmethod
    def find(list_target, func):
        """
        通用查找方法
        :param list_target: 需要查找的列表
        :param func: 查找条件，函数类型
        :return: 需要查找的元素
        """
        for item in list_target:
            """
            调用：具体条件的抽象
            执行：集体条件的函数
            """
            if func(item):
                yield item


    @staticmethod
    def sum(list_target, func_handle):
        sum_val = 0
        for item in list_target:
            sum_val += func_handle(item)
        return sum_val

    @staticmethod
    def select(list_target, func_handle):
        """
        通用筛选方法
        :param list_target:
        :param func_handle:
        :return:
        """
        for item in list_target:
            yield func_handle(item)

    @staticmethod
    def get_max(list_target, func_handle):
        """
        通用获取最大元素方法
        :param list_target:
        :param func_handle:
        :return:
        """
        max_value = list_target[0]
        for item in list_target:
            if func_handle(max_value) < func_handle(item):
                max_value = item
        return max_value

    @staticmethod
    def order_by(list_target, func_handle):
        """
        升序排序
        :param list_target: 需要排序的数据
        :param func_handle: 排序的逻辑
        :return:
        """
        for r in range(len(list_target) - 1):
            for c in range(r + 1, len(list_target)):
                if func_handle(list_target[r]) > func_handle(list_target[c]):
                    list_target[r], list_target[c] = list_target[c], list_target[r]


