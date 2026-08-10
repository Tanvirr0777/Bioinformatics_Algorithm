import sys

t = int(sys.stdin.readline())

for i in range(t):
    a,b,c = map(int, sys.stdin.readline().split())
    mx = max(a,b,c)
    mn = min(a,b,c)
    sm = a+b+c
    print(f"Case {i+1}:" ,sm-(mx+mn))