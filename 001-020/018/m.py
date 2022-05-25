"""
题解：先转为32位的二进制数再比较
"""
import re

A, B, C, D, E, errs, privates = 0, 0, 0, 0, 0, 0, 0


def get_bin(string):
    """
    将点分十进制的IP地址转成二进制的形式
    :param string:点分十进制的IP地址字符串
    :return:物理层的二进制序列字符串
    """
    string_bin = ''
    for i in string.split('.'):
        string_bin += bin(int(i))[2:].rjust(8, '0')
    return string_bin


try:
    while True:
        ip, mask = input().split('~')
        mask_bin = get_bin(mask)
        if ip.split('.')[0] in ('0', '127'):
            continue
        elif mask in ('0.0.0.0', '255.255.255.255'):
            errs += 1
            continue
        else:
            if re.search('01', mask_bin):
                errs += 1
                continue
        ip_bin = get_bin(ip)
        if re.search(r'\.\.', ip):
            errs += 1
        elif get_bin('1.0.0.0') < ip_bin < get_bin('126.255.255.255'):
            A += 1
            if get_bin('10.0.0.0') < ip_bin < get_bin('10.255.255.255'):
                privates += 1
        elif get_bin('128.0.0.0') < ip_bin < get_bin('191.255.255.255'):
            B += 1
            if get_bin('172.16.0.0') < ip_bin < get_bin('172.31.255.255'):
                privates += 1
        elif get_bin('192.0.0.0') < ip_bin < get_bin('223.255.255.255'):
            C += 1
            if get_bin('192.168.0.0') < ip_bin < get_bin('192.168.255.255'):
                privates += 1
        elif get_bin('224.0.0.0') < ip_bin < get_bin('239.255.255.255'):
            D += 1
        elif get_bin('240.0.0.0') < ip_bin < get_bin('255.255.255.255'):
            E += 1
except (EOFError, ValueError):
    pass
print(A, B, C, D, E, errs, privates)
