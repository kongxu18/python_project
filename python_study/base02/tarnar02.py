# 30个 斐波那契数列
def create_fibonacci_series(length):
    """
    输入长度
    :return: 输出数列
    """
    list_fibonacci = [1, 1]
    while len(list_fibonacci) < length:
        number = list_fibonacci[- 1] + list_fibonacci[- 2]
        list_fibonacci.append(number)
    return list_fibonacci


list01 = create_fibonacci_series(10)
print(list01)


# 打印100以内质数
def prime_number(start=1, end=0):
    return [number for number in range(start, end) if check_prime_number(number)]


def check_prime_number(number):
    for item in range(2, number):
        if number % item == 0:
            return False
    return True


print(prime_number())
