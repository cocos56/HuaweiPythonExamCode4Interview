"""
题解3：直接处理
"""
s = input()
count = 0
for i in s:
    if i == ' ':
        count = 0
        continue
    count += 1
print(count)
