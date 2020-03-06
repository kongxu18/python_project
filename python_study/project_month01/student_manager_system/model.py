class StudentModel:
    """
    学生信息模型
    """

    def __init__(self, name='', age=0, score=0, id=0):
        """
        创建学生对象
        :param id: 编号唯一标识
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score
