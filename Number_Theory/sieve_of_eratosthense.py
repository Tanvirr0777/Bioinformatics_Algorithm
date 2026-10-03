import sys

def seive(x):

    prime = [True] * (x + 1)
    prime[0] = prime[1] = False

    p = 2
    while p * p <= x:
        if prime[p]:
            for i in range(p * p, x + 1, p):
                prime[i] = False
        p += 1

    return prime


n = int(sys.stdin.readline())

res = seive(n)

for j in range(2,n + 1):
    if res[j]:
     print(j,end=' ')