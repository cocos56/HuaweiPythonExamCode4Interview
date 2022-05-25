"""
题解2：迭代过程统计余数为1的个数
"""
n = int(input())
# pylint: disable=C0103
c = 0
while n > 0:
    if n % 2:
        c += 1
    n = n // 2
print(c)
