"""
模块相关概念
"""
from module01 import *

fun01()
# 单下划线开头 不能通过 from module01 import * 形式导入，只限于此方法有效
# _fun02()
# from module01 import _fun02
# 可以通过这个形式导入
# _fun02()

"""
    模块成员
"""
# Myclass.fun03()

# 看模块的注释
print(__doc__)

# 模块绝对路径
print(__file__)

# __main__ 判断是否为主模块 不是主模块而是被其他模块导入，存储真名
# 非主模块 ：真名
print(__name__)

# 只有从当前模块运行才会执行，测试代码
# 限制只能从当前模块运行才执行
if __name__ == '__main__':
    list01 = []


"""
模块导入后所有语句都会执行
"""