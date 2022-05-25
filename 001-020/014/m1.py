"""
题解1：使用join方法拼接字符串后统一打印
"""
words = []
for i in range(int(input())):
    words.append(input())
print('\n'.join(sorted(words)))
