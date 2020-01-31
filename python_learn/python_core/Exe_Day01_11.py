"""
模块导入练习
    3种导入方式
"""
import exercise001 as helper


# from exercise001 import *
import exercise001 as helper

list01 = [
    ['00', '01', '02', '03'],
    ['10', '11', '12', '13'],
    ['20', '21', '22', '23'],
]
# re = DoubleListHelper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
# print(re)


re = helper.DoubleListHelper.get_elements(list01, helper.Vector2(1, 0), helper.Vector2.right(), 3)
print(re)