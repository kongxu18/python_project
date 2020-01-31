"""
自定义异常类
"""


class AgeError(Exception):
    """
    封装数据
    """

    def __init__(self, message, age_value, code_line, err_number):
        super().__init__('自定义年纪超大异常：出错了')
        self.message = message
        self.age_value = age_value
        self.code_line = code_line
        self.err_number = err_number


class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 30:
            self.__age = value
        else:
            raise AgeError('太大了', value, 31, 1001)

w01 = Wife(55)
try:
    w01 = Wife(55)
except AgeError as e:
    print(e)
    print(e.message, e.age_value, e.code_line, e.err_number)
    print('重写输入')
