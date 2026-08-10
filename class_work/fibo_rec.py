import sys

def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1) + fibo(num-2)

n = int(sys.stdin.readline())

res = []
for i in range(n):
    res.append(fibo(i))
print(res)