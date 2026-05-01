s = input().strip().lower()

words = s.split()
vowels = "aeiou"

count = 0

for word in words:
    left = 0
    right = len(word) - 1

    while left < right:
        first = word[left]
        last = word[right]

        # check vowel-consonant pair
        if (first in vowels and last not in vowels) or \
            (first not in vowels and last in vowels):
            count += 1

        left += 1
        right -= 1

print(count)