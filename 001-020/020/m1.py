"""
题解1：逐一遍历匹配
"""
while True:
    try:
        password = input()
        # pylint: disable=C0103
        a, b, c, d, flag = 0, 0, 0, 0, True
        for i in password:
            if i.isdigit():  # 或者使用条件：'0' <= i <= '9'
                a = 1
            elif i.islower():  # 或者使用条件：'a' <= i <= 'z'
                b = 1
            elif i.isupper():  # 或者使用条件：'A' <= i <= 'Z'
                c = 1
            else:
                d = 1
        for i in range(len(password) - 3):
            if password.count(password[i:i + 3]) > 1:
                flag = False
                break
        if len(password) > 8 and a + b + c + d >= 3 and flag:
            print("OK")
        else:
            print("NG")
    except EOFError:
        break
