"""
题解2：先格式化字符串再打印
"""
s = input()
for i in range(0, len(s), 8):
    # pylint: disable=C0209
    print('{:0<8s}'.format(s[i:i+8]))
