s = input()
length = 0
for i in s[::-1]:
    if i == ' ':
        break
    length += 1
print(length)
