import sys


word = sys.stdin.readline().strip()

upper = 0
lower = 0

for i in range(len(word)):
    if word[i] == word[i].upper():
        upper += 1
    else:
        lower += 1

if upper > lower:
    print(word.upper())
else:
    print(word.lower())
