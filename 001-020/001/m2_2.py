"""
题解2_2：先逆序再处理_字符串切片功能逆转字符串
"""
s = input()
Length = 0
for i in s[::-1]:
    if i == ' ':
        break
    Length += 1
print(Length)
