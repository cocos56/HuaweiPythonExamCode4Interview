s = input()
length = 0
for i in reversed(s):
    if i == ' ':
        break
    length += 1
print(length)