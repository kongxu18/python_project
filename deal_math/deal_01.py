import sympy

x_array = []

n = sympy.Symbol('n')
result = sympy.summation(2 * n, (n, 1, 100))
print(result)

x = sympy.Symbol('x')
y = sympy.symbols('y')
f = x + 10

# result =x.evalf(subs={f:1})
result = sympy.solve(f - 10, x)
print(result)

import decimal
arr=[]
a=decimal.Decimal('1.5')
arr.append(a)
for i in range(len(arr)):
    arr[i] = float(arr[0])
print(arr)

s=float('43.3749248444531250')
print(s)