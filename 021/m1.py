"""
题解1：逐一情况处理
"""
# pylint: disable=C0103
s = ''
for i in input():
    if 'a' <= i <= 'c':
        s += '2'
    elif 'd' <= i <= 'f':
        s += '3'
    elif 'g' <= i <= 'i':
        s += '4'
    elif 'j' <= i <= 'l':
        s += '5'
    elif 'm' <= i <= 'o':
        s += '6'
    elif 'p' <= i <= 's':
        s += '7'
    elif 't' <= i <= 'v':
        s += '8'
    elif 'w' <= i <= 'z':
        s += '9'
    elif i == 'Z':
        s += 'a'
    elif 'A' <= i < 'Z':
        s += chr(ord(i.lower()) + 1)
    else:
        s += i
print(s)
