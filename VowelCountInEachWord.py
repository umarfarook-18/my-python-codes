s = input().strip().lower()

words = s.split()
vowels = "aeiou"

result = []

for word in words:
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
    result.append(str(count))

print(" ".join(result))