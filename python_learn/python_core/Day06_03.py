"""
    装饰器
"""


# 缺点：增加新功能影响原有功能，违反开闭原则

# 需求：对以下2个功能增加权限验证
# 需要增加功能
# 想要加功能，不改代码
def verify_permissions(func):
    # 星号元组行参 解决调用不统一 多个参数合为元组
    # 双星号形参 ：实参的 关键字参数可以无限传入
    def wrapper(*args, **kwargs):
        print('权限验证')
        # 星号实参 拆分元组
        # 双星号 将获得的字典拆分
        func(*args, **kwargs)

    return wrapper


# 已有功能
# def enter_background():
#     # verify_permissions()
#     """
#         进入后台
#     :return:
#     """
#     print('进入后台')
#
#
# def delete_order():
#     # verify_permissions()
#     """
#         删除订单
#     :return:
#     """
#     print('删除订单')

#
# enter_background = verify_permissions(enter_background)
# delete_order = verify_permissions(delete_order)

# enter_background()
# delete_order()


# 以上还有缺点 ：每次拦截对已有功能调用不科学

@verify_permissions
def enter_background(login_id, pwd):
    # verify_permissions()
    """
        进入后台
    :return:
    """
    print(login_id,pwd,'进入后台')


@verify_permissions
def delete_order(id):
    # verify_permissions()
    """
        删除订单
    :return:
    """
    print(id,'删除订单')


# 这个 其实 调用的是 wapper()
enter_background('abc', 1234)
delete_order(101)

# 以上缺点：如果参数不统一，无法包装
