while False:
    season = input("季度：")
    if season =='春':
        print('1,2,3')
    elif season =='夏':
        print('4,5,6')
    elif season =='秋':
        print('7,8,9')
    else:
        print('10,11,12')

count =0
while count < 5:
    print(count)
    count += 1

first = int(input('first:'))
final = int(input('final:'))
while first < final-1:
    first += 11
    print(first)