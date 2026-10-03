import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
arr = li[:n]

for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
