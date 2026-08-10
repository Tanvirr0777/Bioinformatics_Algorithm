import sys

def factrec(num):
    if num == 0 or num == 1:
        return 1
    return num * factrec(num-1)

n = int(sys.stdin.readline())

print(factrec(n))