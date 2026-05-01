s = input().strip().lower()

words = s.split()
vowels = "aeiou"

vowel_counts = []

for word in words:
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
    vowel_counts.append(count)

min_count = min(vowel_counts)

result = vowel_counts.count(min_count)

print(result)