length_a = 5
count = 0
while False:
    # count < length_a:
    count += 1
    if count == 1 or count == length_a:
        print('*' * length_a + '\n', end='')
    else:
        print('*' + ' ' * (length_a - 2) + '*' + '\n', end='')

# 判断回文
str_input = ''

if str_input == str_input[::-1]:
    print(str_input[::-1] + '是回文')

height = 100
count = 0
way = height
while height > 0.01:
    print(str(height) + '   ', str(count), '  ' + str(way))
    count += 1
    height /= 2
    way += height * 2
