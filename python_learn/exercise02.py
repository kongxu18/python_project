paper =0.01

montuin =8844.43*100*10

count=0

while paper < montuin :
    paper *=2
    count +=1
    print(count, paper)

sum =0
for i in range(101):
    if i%5 !=0:
        continue
    sum +=i
print(sum)

#奇怪的问题
import random

sorce =0
for i in range(3):
    numbe_one =random.randint(1,10)
    numbe_two =random.randint(1,10)
    input = input(str(numbe_one)+'+'+str(numbe_two)+'输入:')
    result = numbe_one + numbe_two
    if int(input)==result:
        sorce+=10
print(sorce)


