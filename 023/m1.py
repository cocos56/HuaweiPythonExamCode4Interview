"""
题解1：追一先比较再打印
"""
dic = {}
s = input()
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
m = min(dic.values())
for i in s:
    if dic[i] > m:
        print(i, end='')
