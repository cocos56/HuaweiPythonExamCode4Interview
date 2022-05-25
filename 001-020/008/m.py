"""
题解：动态构建字典法
"""
n = int(input())
dic = {}
for i in range(n):
    k, v = input().split(' ')
    k = int(k)
    v = int(v)
    if k in dic:
        dic.update({k: dic[k]+v})
    else:
        dic.update({k: v})
for k in sorted(dic, key=lambda x: x):
    print(k, dic[k])
