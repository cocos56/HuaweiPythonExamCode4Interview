"""
题解2：逐位计算值然后累加
"""
s = input()
# pylint: disable=C0103
p = 0
total = 0
for i in s[::-1]:
    if i == 'x':
        break
    elif i == 'A':
        total += 10 * pow(16, p)
    elif i == 'B':
        total += 11 * pow(16, p)
    elif i == 'C':
        total += 12 * pow(16, p)
    elif i == 'D':
        total += 13 * pow(16, p)
    elif i == 'E':
        total += 14 * pow(16, p)
    elif i == 'F':
        total += 15 * pow(16, p)
    else:
        total += int(i) * pow(16, p)
    p += 1
print(total)
