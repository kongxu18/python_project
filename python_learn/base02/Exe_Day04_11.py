"""
    字符串函数
"""
str01 = """ 校 训 ： 自  强不息、厚德载物。  """
# 查找空格数量
print(str01.count(' '))

# 删除字符串前后空格 会生成新字符串
str02 = str01.strip()
print(str02)

# 删除字符串所有空格
str03 = str01.replace(' ', '')
print(str03)

# 查找 载物 的位置
# list01 = list(str01)
# print(len(list01),list01)
print(str01.find('载物'), str01.index('载物'))

# 判断字符串是否以 校训 开头
print(str01.startswith('校训'))

"""
    判读素数函数 
"""


def check_prime_number(number):
    for item in range(2, number):
        if number % item == 0:
            return False
    return True if number > 0 else '因该大于0'


print('----')
result = check_prime_number(15)
print(result)
