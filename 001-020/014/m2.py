"""
题解2：逐个单词遍历时打印
"""
words = []
for i in range(int(input())):
    words.append(input())
words.sort()
for w in words:
    print(w)
