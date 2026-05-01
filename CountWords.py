s = input().strip().lower()

words = s.split()
vowels = "aeiou"

count = 0

for word in words:
    if word[0] in vowels and word[-1] not in vowels:
        count += 1

print(count)