import sys

currency = [0,1,2,4,10,20,40,100,200,400,1000,2000]

r = len(currency) - 1
c = 6000

dp = [ [0]*(c+1) for _ in range(r+1)]

for coin in range(r + 1):
    dp[coin][0] = 1

for coin in range(1,r+1):
    for amount in range(1,c+1):
        if currency[coin] > amount:
            dp[coin][amount] = dp[coin-1][amount]
        else:
            dp[coin][amount] = ( dp[coin-1][amount] +
                                 dp[coin][amount-currency[coin]]
                               )

for line in sys.stdin:
    target_coin = line.strip()

    if float(target_coin) == 0.00:
        break

    dollars, cents = target_coin.split('.')

    cents = int(cents)

    c = int(dollars) * 20 + cents // 5

    print(f"{float(target_coin):6.2f}{dp[r][c]:17d}")


