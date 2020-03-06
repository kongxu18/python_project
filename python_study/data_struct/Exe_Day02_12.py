"""
    利用栈对文本内括号进行匹配检测
"""
text = '[]]{[}'
from lstack import *

# 将验证条件提前定义好
parens = '()[]{}'
left_parens = '([{'
# 验证匹配关系
opposite = {'}': '{', ')': '(', ']': '['}
# 存储括号的栈
ls = LStack()


# 编写生成器，用来遍历字符串，不断的提供括号及其位置
def parent(text):
    i, text_len = 0, len(text)
    #     开始遍历字符串
    while True:
        while i < text_len and text[i] not in parens:
            i += 1
        # 到字符串结尾
        if i >= text_len:
            return
        else:
            yield text[i], i
            i += 1


def ver():
    for pr, i in parent(text):
        if pr in left_parens:
            ls.push((pr, i))
        elif ls.is_empty() or ls.pop()[0] != opposite[pr]:
            print('unmatching is found 上', (i, pr))
            break
    else:
        if ls.is_empty():
            print('完全正常')
        else:
            d = ls.pop()
            print('unmatching is found', (d[1], d[0]))


ver()
