'''

   字典中套字典
'''
dict_stu = {}
while True:
    student = {}
    information = input('name: age: score:')
    if information == '':
        break
    name, age, score = information.split('-')
    student['age'] = age
    student['score'] = score
    dict_stu[name] = student

print(dict_stu)
for name, dict_student in dict_stu.items():
    print(dict_student['age'])
