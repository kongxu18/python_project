import sympy

# 模拟数据
arrx = [2.05191875, 2.0925125, 2.0516625]
epsilon_arrx = [2.05273125, 2.0522875, 2.0847375, ]
arry = [0.000975, 0.00065, 0.000325]
epsilon_arry = [0.008325, 0.00835, 0.008275, 0.008375]

E11 = sympy.Symbol('E11')
E22 = sympy.Symbol('E22')
E12 = sympy.Symbol('E12')


# 直接考虑 E12 =E21
class Sigma:
    def __init__(self, f, n, lower_bound=0, upper_bound=sympy.oo):
        self.f = f
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.n = sympy.Symbol('%s' % n)
        self.arr = []

    def get_result(self):
        result = sympy.summation(self.f, (self.n, self.lower_bound, self.upper_bound))
        return result

    def get_arr_result(self):
        result = sympy.summation(self.f, (self.arr[self.lower_bound], self.lower_bound, len(self.arr)))
        return result


f1 = Sigma('n+1', 'n', 1, 100)
print(f1.get_result())

a11 = sympy.Symbol('a11')
# a11 = Sigma('Nx ** 2', 'Nx', arr=arrx)
# print(a11.get_arr_result())
