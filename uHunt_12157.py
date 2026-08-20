import sys
from math import ceil


def cost_m(x):
    if x < 29:
        return 10
    x -= 29
    cm = ceil(x/30)
    return (cm*10)+10

def cost_j(x):
    if x < 59:
        return 15
    x -= 59
    cj = ceil(x/60)
    return (cj*15)+15


t = int(sys.stdin.readline())

for k in range(t):
    n = int(sys.stdin.readline())
    call = list(map(int, sys.stdin.readline().split()))

    m = 0
    j = 0

    for i in range(n):
        m += cost_m(call[i])
        j += cost_j(call[i])

    if m > j:
        sys.stdout.write(f"Case {k+1}: Juice {j}")
    elif m < j:
        sys.stdout.write(f"Case {k+1}: Mile {m}")
    else:
        sys.stdout.write(f"Case {k+1}: Mile Juice {j}")
    print()