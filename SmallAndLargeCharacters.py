s = input().strip()

words = s.split()

result = []

for word in words:
    result.append(min(word))
    result.append(max(word))

print(" ".join(result))