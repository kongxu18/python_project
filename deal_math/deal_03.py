import sympy
import numpy as np
import pymysql
import math
import decimal

con = pymysql.connect('localhost', 'root', '333333', 'mytest',
                      charset='utf8')
cur = con.cursor()
sql = "select * from 试样5全部应力应变 limit 2700 "
cur.execute(sql)
data = cur.fetchall()
# 四组数据
Nx = []
Epx = []
Ny = []
Epy = []
number = 0
for i in data:
    number += 1
    Nx.append(decimal.Decimal(i[0]))
    Epx.append(decimal.Decimal(i[1]))
    Ny.append(decimal.Decimal(i[2]))
    Epy.append(decimal.Decimal(i[3]))
print(number)

# 模拟数据
arrx = np.array(Nx)
epsilon_arrx = np.array(Epx)
arry = np.array(Ny)
epsilon_arry = np.array(Epy)
print(arrx)
print(epsilon_arrx)

E11 = sympy.Symbol('E11')
E22 = sympy.Symbol('E22')
E12 = sympy.Symbol('E12')

a11 = sum(map(lambda x: pow(x, 2), arrx))
print(a11)
b11 = sum(-2 * arrx * epsilon_arrx)
print(b11, 'b11')

a22 = sum(map(lambda y: pow(y, 2), arry))
print(a22)

b22 = sum(-2 * arry * epsilon_arry)
print(b22, 'b22')

a12 = sum(arrx ** 2 + arry ** 2)
print(a12)

b12 = b11 + b22
print('b12', b12)
a = 2 * sum(arrx * arry)
print(a)

c = sum(epsilon_arry ** 2 + epsilon_arrx ** 2)
print(c)
print('-----')
# 矩阵运算
arry_x = np.mat([[float(2 * a11), float(a), 0], [0, float(a), float(2 * a22)], [float(a), float(2 * a), float(a)]])
print(arry_x)
arry_y = np.mat([[float(-b11)], [float(-b22)], [float(-b12)]])
print(arry_y)

# arr_x=[[43.3749248444531250,43.0119751085156250,0],[0,43.0119751085156250,42.6614448126562500],
#        [43.0119751085156250,86.0239502170312500,43.0119751085156250]]
# arry_y=[0.01345611031250,0.17329597750000,0.18675208781250]
arr_result = np.linalg.solve(arry_x, arry_y)
print(arr_result, '--')
print(np.linalg.inv(arry_x).dot(arry_y))