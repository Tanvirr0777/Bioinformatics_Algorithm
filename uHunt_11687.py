import sys

def digit(num):
    num = str(num)
    return len(num)

f = sys.stdin

for line in f:
    l = line.strip()

    if not l:
        continue

    if l == "END":
        break

    d = len(l)

    res,x = 0,1
    while True:
        if l == "1":
            break
        if d == 1:
            res += 1
            if res == 2:
                break
        x += 1
        d = digit(d)
    print(x)

