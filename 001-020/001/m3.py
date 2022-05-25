"""
题解3：直接处理
"""
s = input()
# pylint: disable=C0103
count = 0
for i in s:
    if i == ' ':
        count = 0
        continue
    count += 1
print(count)
