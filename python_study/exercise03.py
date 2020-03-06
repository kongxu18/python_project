input_number = int(input('输入数字：'))
for item in range(2, input_number):
    result = input_number % item
    if result ==False:
        print('不死素数')
        break
else:
    print('素数')


