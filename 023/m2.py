"""
题解2：先统一替换再打印
"""
s = input()
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
m = min(dic.values())
for i, value in dic.items():
    if value == m:
        s = s.replace(i, '')
print(s)
