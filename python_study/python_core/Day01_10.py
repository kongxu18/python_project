# import module01
#
# module01.fun01()
# my02 =module01.Module()
# my02.fun02()

"""
导入方式二
"""
from module01 import Module
from module01 import fun01

fun01()
my02 = Module()
my02.fun02()

from module01 import *