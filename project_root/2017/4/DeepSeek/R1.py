import sys

passphrases = []
with open(sys.argv[1]) as f:
    passphrases = [line.strip() for line in f]

first = 0
second = 0

for line in passphrases:
    words = line.split()
    n = len(words)
    seen1 = set()
    valid1 = True
    for word in words:
        if word in seen1:
            valid1 = False
            break
        seen1.add(word)
    if valid1:
        first += 1
        
    seen2 = set()
    valid2 = True
    for word in words:
        sorted_tuple = tuple(sorted(word))
        if sorted_tuple in seen2:
            valid2 = False
            break
        seen2.add(sorted_tuple)
    if valid2:
        second += 1

print(first)
print(second)