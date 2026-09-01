import sys

n = int(sys.stdin.readline())

temp_str = sys.stdin.readline()

game = temp_str[:n].upper()

anton = 0
danik = 0

for char in game:
    if char == 'A':
        anton += 1
    else:
        danik += 1

if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
else:
    print("Friendship")

