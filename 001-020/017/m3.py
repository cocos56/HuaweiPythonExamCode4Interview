"""
题解3：穷举判断
"""
x, y = 0, 0
for i in input().split(';'):
    if not 2 <= len(i) <= 3:
        continue
    if not '0' <= i[1] <= '9':
        continue
    if len(i) == 3 and not '0' <= i[2] <= '9':
        continue
    direction, step = i[0], int(i[1:])
    if direction == 'A':
        x -= step
    elif direction == 'D':
        x += step
    elif direction == 'S':
        y -= step
    elif direction == 'W':
        y += step
print(f'{x},{y}')
