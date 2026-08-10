import sys

def emoogle_balance(e):
    event = 0
    l = len(e)
    for i in range(len(e)):
        if 0 < e[i] < 100:
             event += 1
        else:
            continue
    return 2*event - l

f = sys.stdin
i = 1
for line in f:
    n = int(line)
    if n == 0:
        break
    data = list(map(int, input().split()))
    arr = data[:n]
    print(f"Case {i}: {emoogle_balance(arr)}")
    i += 1

