"""
题解3：递归
"""
import sys


def function(n):
    if n >= 2:
        return function(n - 2) + 1
    else:
        return 0


if __name__ == '__main__':
    data = sys.stdin
    for x in data:
        x = int(x.strip())
        if x:
            print(function(x))
