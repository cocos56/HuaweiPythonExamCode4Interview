"""
题解2_1：先逆序再处理_使用reverse函数
"""
# pylint: disable=C0103
length = 0
for i in reversed(input()):
    if i == ' ':
        break
    length += 1
print(length)
