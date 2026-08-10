import sys

word = sys.stdin.readline().strip()

char = word[0].upper()
temp = word[1:]

res = char + temp

print(res)