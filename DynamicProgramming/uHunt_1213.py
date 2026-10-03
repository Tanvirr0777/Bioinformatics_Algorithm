import sys

MAX_l = 1120

def seive():
    prime = [True]* (MAX_l + 1)

    p = 2
    while p*p <= MAX_l+1:
        if prime[p]:
            for i in range(p**2, MAX_l+1, p):
                prime[i] = False
        p +=1

    res = []
    for j in range(2,MAX_l+1):
       if prime[j]:
          res.append(j)
    return res

primes = seive()
dp = [[0]* (MAX_l+1) for _ in range(15)]

dp[0][0] = 1


for prime in primes:
    for times in range(14,0,-1):
        for sm in range(MAX_l,prime-1,-1):
            dp[times][sm] += dp[times-1][sm-prime]

for line in sys.stdin:
    n,k = map(int,line.split())

    if n == 0 and k == 0:
        break

    print(dp[k][n])