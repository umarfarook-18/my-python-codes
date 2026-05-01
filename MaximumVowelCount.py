s = input().strip().lower()

words = s.split()
vowels = "aeiou"

max_count = 0

for word in words:
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
    if count > max_count:
        max_count = count

print(max_count)