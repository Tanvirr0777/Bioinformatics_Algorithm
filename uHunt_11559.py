import sys

f = sys.stdin

while True:
    try:
        a,b,c,d = map(int,f.readline().split())

        cost = float('Inf')

        for _ in range(c):
            price_room = int(sys.stdin.readline())
            bed_w = list(map(int,sys.stdin.readline().split()))

            if max(bed_w) >= a:
                cost = min(cost, a * price_room)

        if cost <= b :
            print(cost)
        else:
            print("stay home")

    except ValueError:
        break

