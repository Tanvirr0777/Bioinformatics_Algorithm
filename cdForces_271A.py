import sys

def distinct(x,l):
    s = list(set(x))
    if len(s) == l:
        return True
    else:
        return False

arr = []
y = int(sys.stdin.readline())
a = y + 1

res = False
while not res:
    b = str(a)
    l = len(b)
    res = distinct(b,l)

    if res:
        arr.append(1)
        break
    else:
        arr.append(0)
        a += 1
        continue

print(y+len(arr))

