"""
题解：使用字典处理
"""
dic = {}
try:
    while True:
        p, n = input().split(' ')
        name = p.split('\\')[-1][-16:]
        key = name + ' ' + n
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1
except (EOFError, ValueError):
    keys = list(dic)[-8:]
    for k in keys:
        print(k, dic[k])
