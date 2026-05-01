s = input().strip()

words = s.split()

for i in range(len(words)):
    if i % 2 == 0:   # even index
        words[i] = words[i][::-1]

print(" ".join(words))