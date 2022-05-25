"""
题解3：直接处理
"""
# pylint: disable=C0103
cnt = 0
for i in input():
    if i == ' ':
        cnt = 0
        continue
    cnt += 1
print(cnt)
