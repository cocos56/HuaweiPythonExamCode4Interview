"""
题解2_1：先逆序再处理_使用reverse函数
"""
s = input()
length = 0
for i in reversed(s):
    if i == ' ':
        break
    length += 1
print(length)
