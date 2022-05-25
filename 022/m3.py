"""
题解3：递归
"""
import sys


def f(n):
    if n >= 2:
        return f(n - 2) + 1
    else:
        return 0


if __name__ == '__main__':
    data = sys.stdin
    for x in data:
        x = int(x.strip())
        if x:
            print(f(x))
