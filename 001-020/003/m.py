"""
题解：使用集合自动去重
"""
s = set()
for i in range(int(input())):
    s.add(int(input()))
for i in sorted(s):
    print(i)
