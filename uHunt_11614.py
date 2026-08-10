import sys
from math import floor

n = int(sys.stdin.readline())

for i in range(n):
    s = int(sys.stdin.readline())

    l = floor(( -1 + (1+8*s)**0.5 ) // 2)
    print(l)

