s = input().strip().lower()

vowels = "aeiou"
count = 0

left = 0
right = len(s) - 1

while left < right:
    a = s[left]
    b = s[right]

    # check both are letters
    if a.isalpha() and b.isalpha():
        if (a in vowels and b not in vowels) or \
           (a not in vowels and b in vowels):
            count += 1

    left += 1
    right -= 1

print(count)