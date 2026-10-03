import sys

bills = [100,20,10,5,1]

amount = int(sys.stdin.readline())

bill = 0

i = 0
while amount > 0:

    cost = amount // bills[i]
    bill += cost

    amount -= cost * bills[i]

    if amount < bills[i]:
        i += 1

print(bill)