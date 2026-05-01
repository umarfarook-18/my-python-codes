s = input().strip()

words = s.split()

# Reverse each word
for i in range(len(words)):
    words[i] = words[i][::-1]

# Reverse word positions
words = words[::-1]

print(" ".join(words))