import sys

currency = [0,1,5,10,25,50]

r = len(currency) - 1
c = 30000

dp = [ [0]*(c+1) for _ in range(r+1)]

for coin in range(r + 1):
    dp[coin][0] = 1

for coin in range(1,r+1):
    for amount in range(1,c+1):
        if currency[coin] > amount:
            dp[coin][amount] = dp[coin-1][amount]
        else:
            dp[coin][amount] =  dp[coin-1][amount] + dp[coin][amount-currency[coin]]

for line in sys.stdin:
    target_coin = line.strip()

    find = int(target_coin)

    if dp[r][find] == 1:
        print(f"There is only 1 way to produce {find} cents change.")
    else:
        print(f"There are {dp[r][find]} ways to produce {find} cents change.")