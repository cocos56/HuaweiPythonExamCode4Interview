"""
题解2_1：先逆序再处理_使用reverse函数
"""


def get_length():
    string = input()
    length = 0
    for i in reversed(string):
        if i == ' ':
            break
        length += 1
    print(length)


get_length()
