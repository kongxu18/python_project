"""
外部嵌套作用域

"""


def fun01():
    # 是fun01 函数局部作用域
    # 也是fun02 函数外部嵌套作用域
    a = 1
    c = 1

    def fun02():
        # 可以访问外部嵌套作用域变量
        # 不能访问外部嵌套作用域变量
        b = 2
        # 创建了fun02 的局部变量
        a = 2
        # 声明外部嵌套作用域
        nonlocal c
        c = 3
        print(a,c)
    fun02()
    print(a,c)


fun01()
