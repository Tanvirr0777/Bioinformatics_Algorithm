import sys

t = int(sys.stdin.readline())

for _ in range(t):

   n = int(sys.stdin.readline())

   coins = list(map(int, sys.stdin.readline().split()))

   diff_coins = 1
   sum_coins = coins[0]

   for i in range(1, len(coins)-1):
       if sum_coins + coins[i] <= coins[i+1]:
           sum_coins += coins[i]
           diff_coins += 1

   if len(set(coins)) == 1:
       print(1)
   else:
       print(diff_coins+1)



