s = input()
words = s.split()
min_length = min(len(word) for word in words)
print(min_length)