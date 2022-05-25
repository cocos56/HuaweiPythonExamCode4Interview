"""
题解2：遍历字符串，逐一比较
"""
s = input().upper()
c = input().upper()
cnt = 0
for i in s:
    if c == i:
        cnt += 1
print(cnt)
