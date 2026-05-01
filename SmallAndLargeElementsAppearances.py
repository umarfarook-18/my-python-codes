s = input().strip()

filtered = []

for ch in s:
    if ch.isalnum():
        filtered.append(ch)

min_char = min(filtered)
max_char = max(filtered)

min_count = filtered.count(min_char)
max_count = filtered.count(max_char)

print(min_char, min_count, max_char, max_count)