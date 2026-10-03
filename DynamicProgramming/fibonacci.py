import sys


def dpfibonacci(n,dp):

    if n == 0 or n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = dpfibonacci(n - 1,dp) + dpfibonacci(n - 2,dp)
    return dp[n]

n = int(sys.stdin.readline())

dp = [-1] * (n+1)

for i in range(n+1):
    print(dpfibonacci(i,dp), end=" ")





