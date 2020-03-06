dict_hobbies = {}
while True:
    name = input('name：')
    count = 1
    if name == ' ':
        break
    list_hobbies = []
    while True:
        hobbies = input('%d hobby' % count)
        count += 1
        if hobbies == '':
            break
        list_hobbies.append(hobbies)
    dict_hobbies[name] = list_hobbies

print(dict_hobbies)