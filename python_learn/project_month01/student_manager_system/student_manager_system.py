"""
学生管理系统
"""


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


class StudentManagerController:
    """
    学生管理控制器，负责业务逻辑处理
    """

    # 类变量初始化编号
    __init_id = 0

    def __init__(self):
        self.__stu_list = []
        # self.stu_list=[]

    @property
    def stu_list(self):
        """

        :return:
        """
        return self.__stu_list

    def add_student(self, stu_info):
        """
        添加一个学生
        :param stu_info:
        :return:
        """
        stu_info.id = self.__generate_id()
        self.stu_list.append(stu_info)

    """
    要不要用静态
    """

    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, id):
        """
        移除学生信息
        :param id:
        :return:
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
        return False

    def update_student(self, stu_info):
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        # self.__stu_list
        """
        进行排序
        :return:
        """
        for r in range(len(self.__stu_list) - 1):
            for c in range(r + 1, len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c], self.__stu_list[r]


manager = StudentManagerController()

s01 = StudentModel('张三', 24, 100)
s02 = StudentModel('李四', 22, 99)

manager.add_student(s01)
manager.add_student(s02)
for item in manager.stu_list:
    print(item.name, item.id, item.age, item.score)
manager.update_student(StudentModel('修改人', 0, 0, 1))
# manager.remove_student(2)
for item in manager.stu_list:
    print(item.name, item.id, item.age, item.score)


class StudrntManagerView:
    """
    视图
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    @staticmethod
    def __display_menu():
        print('1)添加学生')
        print('2)显示学生')
        print('3)删除学生')
        print('4)修改学生')
        print('5)排序学生')

    def __select_menu(self):
        item = input('请输入')
        if item == '1':
            self.__input_student()
        elif item == '2':
            self.__output_students(self.__manager.stu_list)
        elif item == '3':
            self.__delete__student()
        elif item == '4':
            self.__modify_student()
        elif item == '5':
            self.__output_students_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input('name:')
        age = input('age:')
        score = input('score:')
        stu = StudentModel(name, int(age), int(score))
        self.__manager.add_student(stu)

    def __output_students(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    def __delete__student(self):
        id = int(input('编号：'))
        if self.__manager.remove_student(id):
            print('删除成功')
        else:
            print('失败')

    def __modify_student(self):
        id = input('编号:')
        name = input('name:')
        age = input('age:')
        score = input('score:')
        stu = StudentModel(name, int(age), int(score), int(id))
        if self.__manager.update_student(stu):
            print('成功')
        else:
            print('失败')

    def __output_students_by_score(self):
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)


view = StudrntManagerView()
view.main()
