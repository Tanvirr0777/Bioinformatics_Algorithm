import sys

t = int(sys.stdin.readline())

for case in range(t):

    n,p,q = map(int, sys.stdin.readline().split())
    egg = list(map(int, sys.stdin.readline().split()))

    total = 0
    weight = 0

    l = min(n,p)
    for i in range(l):
        weight += egg[i]
        total += 1

    l = l-1
    while l >= 0:
        if weight <= q and total <= p:
           break
        else:
            weight -= egg[l]
            total -= 1
        l -= 1

    print(f"Case {case+1}: {total}")
