"""
题解：字符串逆序打印前先查重
"""
n = input()[::-1]
s = set()
for i in n:
    if i not in s:
        print(i, end='')
    s.add(i)
