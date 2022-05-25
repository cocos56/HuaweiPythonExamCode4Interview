"""
题解1：逐一遍历匹配
"""
while True:
    try:
        pw = input()
        # pylint: disable=C0103
        a, b, c, d, flag = 0, 0, 0, 0, True
        for i in pw:
            if i.isdigit():  # 或者使用条件：'0' <= i <= '9'
                a = 1
            elif i.islower():  # 或者使用条件：'a' <= i <= 'z'
                b = 1
            elif i.isupper():  # 或者使用条件：'A' <= i <= 'Z'
                c = 1
            else:
                d = 1
        for i in range(len(pw) - 3):
            if pw.count(pw[i:i + 3]) > 1:
                flag = False
                break
        if len(pw) > 8 and a + b + c + d >= 3 and flag:
            print("OK")
        else:
            print("NG")
    except EOFError:
        break
