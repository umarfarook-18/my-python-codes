s = input().strip()

words = s.split()

first_word = words[0]
last_word = words[-1]

print(min(first_word), max(last_word))