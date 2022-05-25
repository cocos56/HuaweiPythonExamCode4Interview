"""
题解2：提前建映射表
"""
A = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
B = '22233344455566677778889999bcdefghijklmnopqrstuvwxyza'
c = ''
for i in input():
    if i in a:
        c += b[a.index(i)]
    else:
        c += i
print(c)
