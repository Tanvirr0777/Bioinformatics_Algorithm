import sys


n,k = map(int, sys.stdin.readline().split())

while k > 0:
    if n % 10 != 0:
        n -= 1
    else:
        n = n // 10
    k -= 1
print(n)