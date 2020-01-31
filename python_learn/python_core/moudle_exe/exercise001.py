class Vector2:
    """
    二维向量，表示方向
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 函数表示方向
    @staticmethod
    def left():
        """DoubleListHelper
        静态方法 对数据的处理
        :return:
        """
        return Vector2(0, -1)

    @staticmethod
    def right():
        """
        表达右边
        :return:
        """
        return Vector2(0, 1)

    @staticmethod
    def up():
        """
        往上移动
        :return:
        """
        return Vector2(-1, 0)

    @staticmethod
    def down():
        """
        向下移动
        :return:
        """
        return Vector2(1, 0)


class DoubleListHelper:
    @staticmethod
    def get_elements(target, vect_pos, vect_dir, count):
        """
        获取指定位置，指定方向的，指定数量的元素
        :return:
        """
        list_result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result


# 只有从当前模块运行才会执行
if __name__ == '__main__':
    list01 = []
