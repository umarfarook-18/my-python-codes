s = input().strip()

vowels = "aeiouAEIOU"
result = []

for word in s.split():
    consonants = []

    # collect consonants
    for ch in word:
        if ch not in vowels:
            consonants.append(ch)

    consonants.sort()

    new_word = ""
    idx = 0

    for ch in word:
        if ch in vowels:
            new_word += ch
        else:
            new_word += consonants[idx]
            idx += 1

    result.append(new_word)

print(" ".join(result))