import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    n,k = map(int, sys.stdin.readline().split())
    land = sys.stdin.readline()

    loop_run = math.ceil(n / k)

    nhoj_land = 0

    j,initial,limit = 0,0,k
    while j < loop_run:

        temp = land[initial:limit]
        if '0' not in temp:
            nhoj_land += 1
        initial += k
        limit += k
        temp = ""

        j += 1

    print(nhoj_land)