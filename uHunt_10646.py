import sys

t = int(sys.stdin.readline())

for j in range(t):

    card = []

    while len(card) < 52:
        card += sys.stdin.readline().split()

    rem_card = card[:]

    y = 0
    for i in range(0, 3):
        x = 0
        temp = rem_card[0]
        value = temp[0]

        if value.isdigit() and 1 <= int(value) <= 9:
            x = int(value)
        else:
            x = 10
        y += x
        rem_card = rem_card[11-x:]
    print(f"Case {j+1}: {rem_card[y-1]}")