"""
题解3：先填充0再统一打印
"""
try:
    while True:
        s = input()
        length = len(s)
        if not length % 8 == 0:
            for i in range(8 - length % 8):
                s += '0'
        cnt = 0
        for i in s:
            cnt += 1
            if not cnt % 8:
                print(i)
            else:
                print(i, end='', sep='')
except EOFError:
    pass
