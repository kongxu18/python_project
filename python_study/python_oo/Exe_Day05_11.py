"""
定义员工管理器
    1，管理所有员工
    2，计算所有员工工资
    员工岗位：
        销售：
        测试：
"""


class EmployeeManager:
    def __init__(self):
        self.__employees = []

    # @property
    # def employees(self):
    #     return self.__employees
    #
    # @employees.setter
    # def employees(self, value):
    #     self.__employees = value

    def add_employee(self, emp):
        self.__employees.append(emp)

    def calculate(self):
        total_saraly = 0
        for item in self.__employees:
            total_saraly += item.calculate_salary()
        return total_saraly


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # return self.bonus + self.base_salary
        # 使用扩展重写，先使用爸爸的，在写自己的
        return super().calculate_salary() + self.bonus


man = EmployeeManager()
man.add_employee(Programmer(200000, 1000))
a = man.calculate()
print(a)
