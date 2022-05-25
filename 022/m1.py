"""
题解1：自迭代
"""
while True:
    n = int(input())
    if not n:
        break
    # pylint: disable=C0103
    b = 0
    while n > 1:
        if n == 2:
            b += 1
            break
        t = n // 3
        n = t + n % 3
        b += t
    print(b)
