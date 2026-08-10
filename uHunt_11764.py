import sys

def hjump(a,s):
    x,y = 0,1
    counth = 0
    countl = 0
    while y < s:
        if a[x] < a[y]:
            counth += 1
        if a[x] > a[y]:
            countl += 1
        x += 1
        y += 1
    return counth, countl

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    arr = data[0:n]
    h,l = hjump(arr,n)
    print(f"Case {i+1}: {h} {l}")