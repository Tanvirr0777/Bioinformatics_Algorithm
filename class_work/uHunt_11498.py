import sys

while True:

    t = int(sys.stdin.readline())

    if t == 0:
        break

    ox, oy = map(int, sys.stdin.readline().split())
    r = t
    while r > 0:
        x,y = map(int, sys.stdin.readline().split())
        if x > ox and y > oy:
            print("NE")
        elif x < ox and y > oy:
            print("NO")
        elif x < ox and y < oy:
            print("SO")
        elif x > ox and y < oy:
            print("SE")
        else:
            print("divisa")
        r -= 1


