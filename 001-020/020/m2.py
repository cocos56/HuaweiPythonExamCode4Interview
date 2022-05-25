"""
题解2：使用正则匹配
"""
import re


def check_pw(pw):
    if len(pw) < 8:
        return False
    mix_types = 0
    if re.search(r'\d', pw):  # 匹配数字还可以使用'[0-9]'
        mix_types += 1
    if re.search('[a-z]', pw):
        mix_types += 1
    if re.search('[A-Z]', pw):
        mix_types += 1
    if re.search('[^0-9a-zA-Z]', pw):
        mix_types += 1
    if mix_types < 3:
        return False
    for i in range(len(pw) - 3):
        if pw.count(pw[i:i + 3]) > 1:  # 或者使用len(pw.split(pw[i:i+3])) > 2
            return False
    return True


try:
    while True:
        print('OK' if check_pw(input()) else 'NG')
except (EOFError, ValueError):
    pass
