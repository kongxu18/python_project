from bll import StudentManagerController
from model import StudentModel


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
        age = self.__input_number('age:')
        score = self.__input_number('score:')
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    @staticmethod
    def __input_number(message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                print('输入有误')

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
