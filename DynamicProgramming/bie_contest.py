import sys

coins = [0,57,71,87,97,99,101,103,113,114,115,128,129,137,131,137,147,156,163,186]

row = len(coins) - 1
col = 10000

dp = [ [0]*(col+1) for _ in range(row+1) ]

dp[0][0] = 1

for i in range(row+1):
    dp[i][0] = 1

for i in range(1,row+1):
    for j in range(1,col+1):
       if coins[i] > j:
           dp[i][j] = dp[i-1][j]
       else:
           dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]


t = int(sys.stdin.readline())

amount = []

for _ in range(t):
 target = int(sys.stdin.readline())
 amount.append(target)

for find in amount:
    print(dp[row][find])