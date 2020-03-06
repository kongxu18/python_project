'''
    闰年
'''
list_leap_year = [year for year in range(1970, 2051) if year % 4 == 0 and year % 100 != 0]
print(list_leap_year)

'''
字典
'''
dict_city = {'北京': {'景区': ['谷歌', '天安门'], '美食': ['烤鱼', '烤鸭']}
    , '上海': {'景区': ['谷歌', '天安门'], '美食': ['烤鱼', '烤鸭']}}
print(dict_city)

'''
字符串计数
'''
str_count = 'abcdefce'
list_count = []
dict_count = {}
for item in str_count:
    list_count.append(item)
print(list_count)
for item in list_count:
    count = list_count.count(item)
    dict_count[item] = list_count.count(item)
print(dict_count)

'''

纯用字典
'''
for item in str_count:
    if item not in dict_count:
        dict_count[item] = 1
    else:
        dict_count[item] += 1

