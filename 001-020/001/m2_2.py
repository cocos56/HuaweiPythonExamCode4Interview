"""
题解2_2：先逆序再处理_字符串切片功能逆转字符串
"""
# pylint: disable=C0103
length = 0
for i in input()[::-1]:
    if i == ' ':
        break
    length += 1
print(length)
