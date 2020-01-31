"""
包 package
    将模块以文件夹形式进行分组管理
    __init__ 文件会在包加载时候自动调用
"""

# from package01.module_a import *
# fun01()
#
# from package01.package02.module_b import *
# fun02()

from package01 import *
# 依赖于在包中__init__ 中指定__all__
module_a.fun01()


import sys
sys.path.append('')
"""
    搜索顺序
"""
print(sys.path)

