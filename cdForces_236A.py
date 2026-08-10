import sys

user = sys.stdin.readline().strip()

distinct_char = []

for char in user:
    if char not in distinct_char:
        distinct_char.append(char)

if len(distinct_char) % 2 != 0 :
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")