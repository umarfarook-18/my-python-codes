s = input()

count = 0

for ch in s:
    if 'a' <= ch <= 'z':
        count += 1

print(count)