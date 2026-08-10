import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = list(map(int, sys.stdin.readline().split()))
    r = sorted(n)
    print(f"Case {i+1}:" ,r[1])
