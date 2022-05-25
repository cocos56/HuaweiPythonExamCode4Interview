"""
题解1：使用ljust方法，不断自迭代打印
"""
try:
    while True:
        s = input()
        while len(s):
            print(s[:8].ljust(8, '0'))
            s = s[8:]
except EOFError:
    pass
