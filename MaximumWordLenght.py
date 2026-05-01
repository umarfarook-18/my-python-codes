s = input()
words = s.split()
max_length = max(len(word) for word in words)
print(max_length)