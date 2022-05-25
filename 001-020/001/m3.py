"""
题解3：直接处理
"""
s = input()
cnt = 0
for i in s:
    if i == ' ':
        cnt = 0
        continue
    cnt += 1
print(cnt)
