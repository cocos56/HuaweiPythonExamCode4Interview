"""
题解3：递归
"""
import sys


def function(number):
    """
    递归方法
    :param number: 空气瓶数量
    :return: 最多可以喝的气瓶数
    """
    if number >= 2:
        return function(number - 2) + 1
    else:
        return 0


if __name__ == '__main__':
    data = sys.stdin
    for x in data:
        x = int(x.strip())
        if x:
            print(function(x))
