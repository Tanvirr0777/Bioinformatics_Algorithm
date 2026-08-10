import sys

def sumarray(array):
    return sum(array)

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    arr = lst[:n]

    i = 0
    for i in range(0,n):
        if i == n-1:
          break
        if  sumarray(arr) == 0:
            sys.stdout.write("YES" + "\n")
            break

        if sumarray(arr) % 4 == 0:
            sys.stdout.write("YES" + "\n")
            break
    if i == n-1:
        sys.stdout.write("NO" + "\n")
print()