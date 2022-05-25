"""
题解：先转为32位的二进制数再比较
"""
import re

A, B, C, D, E, errs, privates = 0, 0, 0, 0, 0, 0, 0


def getBin(string):
    string_bin = ''
    for i in string.split('.'):
        string_bin += bin(int(i))[2:].rjust(8, '0')
    return string_bin


try:
    while True:
        ip, mask = input().split('~')
        mask_bin = getBin(mask)
        if ip.split('.')[0] in ('0', '127'):
            continue
        elif mask in ('0.0.0.0', '255.255.255.255'):
            errs += 1
            continue
        else:
            if re.search('01', mask_bin):
                errs += 1
                continue
        ip_bin = getBin(ip)
        if re.search(r'\.\.', ip):
            errs += 1
        elif getBin('1.0.0.0') < ip_bin < getBin('126.255.255.255'):
            A += 1
            if getBin('10.0.0.0') < ip_bin < getBin('10.255.255.255'):
                privates += 1
        elif getBin('128.0.0.0') < ip_bin < getBin('191.255.255.255'):
            B += 1
            if getBin('172.16.0.0') < ip_bin < getBin('172.31.255.255'):
                privates += 1
        elif getBin('192.0.0.0') < ip_bin < getBin('223.255.255.255'):
            C += 1
            if getBin('192.168.0.0') < ip_bin < getBin('192.168.255.255'):
                privates += 1
        elif getBin('224.0.0.0') < ip_bin < getBin('239.255.255.255'):
            D += 1
        elif getBin('240.0.0.0') < ip_bin < getBin('255.255.255.255'):
            E += 1
except (EOFError, ValueError):
    pass
print(A, B, C, D, E, errs, privates)
