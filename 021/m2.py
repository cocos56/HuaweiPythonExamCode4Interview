"""
题解2：提前建映射表
"""
A = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
B = '22233344455566677778889999bcdefghijklmnopqrstuvwxyza'
# pylint: disable=C0103
c = ''
for i in input():
    if i in A:
        c += B[A.index(i)]
    else:
        c += i
print(c)
