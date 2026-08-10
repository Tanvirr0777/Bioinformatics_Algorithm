import sys

def sum_rec(num):
    if num == 1:
        return 1
    return num + sum_rec(num-1)

n = int(sys.stdin.readline())

res = sum_rec(n)

print(res)