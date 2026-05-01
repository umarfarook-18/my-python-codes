s = input().strip()

vowels = ['a', 'e', 'i', 'o', 'u']

missing = []

for v in vowels:
    if v not in s:
        missing.append(v)

if len(missing) == 0:
    print(0)
else:
    print(" ".join(missing))