'''
集合
'''
set01 = {1, 2, 3}
set02 = {4, 2, 3}
# 交集 并 补
set01 & set02
set01 | set02
set01 ^ set02  # -

str_test = 'sadddfdfasdf'
set_str = set(str_test)
print(set_str)

dict_test = {'经理': {'曹操', '刘备', '孙权'},
             '技术': {'曹操', '刘备', '张飞', '关羽'}}

set_Jl = dict_test['经理']
set_Js = dict_test['技术']

# 是经理  技术
set01 = set_Jl & set_Js
print(set01)
# 是经理 不 技术
set02 = set_Jl - set_Js
print(set02)
# 是技术 不 经理
set03 = set_Js - set_Jl
print(set03)
# 张飞是否经理
print('张飞' in set_Jl)
# 身兼一职
set04 = set_Jl ^ set_Js
print(set04)
# 经理和技术一共人数
print(len(set_Jl | set_Js))
