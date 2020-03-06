"""
    闭包
    三要素 ：
        必须要一个内嵌函数
        内嵌函数必须引用外部函数中变量
        外部函数返回值必须是内嵌函数
    fun01调用完成并不会立即释放栈帧，而是等fun02执行完毕

    函数作为返回值：逻辑连续，当内部函数被调用时，不脱离当前的逻辑
"""


def fun01():
    a = 1

    def fun02():
        print(a)
        # return a

    # 不要括号
    return fun02


# 调用外部函数，返回值是内嵌函数
result = fun01()
# 调用内部函数，可以访问外部变量
result()

"""
    闭包的应用
"""


def give_gife_money(money):
    """
    得到压岁钱
    :param money:
    :return:
    """
    print('压岁钱%d' % money)

    def child_buy(target, price):
        nonlocal money
        if money >= price:
            money -= price
            print('花费%d，购买了%s' % (price, target))
        else:
            print('no money')

    return child_buy


action = give_gife_money(10000)
action('唐僧肉', 1000)
