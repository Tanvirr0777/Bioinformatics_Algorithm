import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    res = ((((((n * 567) // 9) + 7492) * 235) // 47) - 498)

    if res < 0:
        res = res * (-1)
        res = res // 10
    else:
        res = res // 10

    print(res % 10)