s = input()

count = 0

for ch in s:
    if not ch.isalnum() and ch != ' ':
        count += 1

print(count)