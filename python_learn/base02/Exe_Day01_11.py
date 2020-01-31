arr_list = list()
while True:
    input_str = input('输入：')
    if input_str == '':
        break
    arr_list.append(input_str)
print(''.join(arr_list))

str_english = 'how are you'
list_temp = str_english.split(' ')
result = list_temp[::-1]
# for i in range(len(str_list)-1,-1,-1):
#     result.append(str_list[i])
print(' '.join(result))
