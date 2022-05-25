"""
题解2：使用正则匹配
"""
import re


def check_pw(password):
    """
    检查密码
    :param password: 密码
    :return: 是否合格
    """
    if len(password) < 8:
        return False
    mix_types = 0
    if re.search(r'\d', password):  # 匹配数字还可以使用'[0-9]'
        mix_types += 1
    if re.search('[a-z]', password):
        mix_types += 1
    if re.search('[A-Z]', password):
        mix_types += 1
    if re.search('[^0-9a-zA-Z]', password):
        mix_types += 1
    if mix_types < 3:
        return False
    for i in range(len(password) - 3):
        if password.count(password[i:i + 3]) > 1:  # 或者使用len(pw.split(pw[i:i+3])) > 2
            return False
    return True


try:
    while True:
        print('OK' if check_pw(input()) else 'NG')
except (EOFError, ValueError):
    pass
