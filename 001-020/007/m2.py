"""
题解2：判断十分位是否满足进位条件
"""
n = float(input())
if n*10 % 10 >= 5:
    print(int(n)+1)
else:
    print(int(n))
