"""
题解2：先格式化字符串再打印
"""
try:
    while True:
        s = input()
        for i in range(0, len(s), 8):
            print('{:0<8s}'.format(s[i:i+8]))
except EOFError:
    pass