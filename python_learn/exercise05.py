list01 =[1,2,3,4,5,6,7,8,9,10]
list02=[]
for item in list01:
    if item >5 :
        list02.append(item)
print(list02)


list03 = []
while True:
    number = input('数字')
    if number =='':
        break
    list03.append(int(number))


frist=list03[0]
for item in list03:
    if item > frist:
        frist =item
print(frist)

