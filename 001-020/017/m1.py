"""
题解1：正则+lambda
"""
import re

x, y = 0, 0
fun = {
    'A': lambda a, b, p: (a - p, b),
    'D': lambda a, b, p: (a + p, b),
    'W': lambda a, b, p: (a, b + p),
    'S': lambda a, b, p: (a, b - p)
}
for cmd in input().split(';'):
    if re.search(r'[ASWD]\d+$', cmd) and 2<=len(cmd) <= 3:
        x, y = fun[cmd[0]](x, y, int(cmd[1:]))
print(f'{x},{y}')
