"""
题解4：先打印输入的字符串，再打印需要填充的0
"""
while True:
    try:
        cnt = 0
        for i in input():
            if cnt % 8 == 0 and cnt:
                print()
            print(i, sep='', end='')
            cnt += 1
        zN = 8 - cnt % 8
        if zN == 8:
            continue
        for i in range(zN):
            print('0', sep='', end='')
        print()
    except EOFError:
        break
