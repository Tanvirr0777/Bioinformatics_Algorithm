import sys

t = int(sys.stdin.readline())

for i in range(t):
    data = list(map(int, sys.stdin.readline().split()))
    n = data[0]
    arr = data[1:n+1]
    print(f"Case {i+1}:",max(arr))