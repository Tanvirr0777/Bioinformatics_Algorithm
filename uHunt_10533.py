import sys

MAX_L = 1000000

# sieve of erotosthense
prime = [True] * (MAX_L + 1)
prime[0] = prime[1] = False

p = 2
while p * p <= MAX_L:
    if prime[p]:
       for i in range(p * 2, MAX_L + 1, p):
         prime[i] = False
    p += 1

# sum of digit count
def sumdigit(y):
    sm = 0
    while y != 0:
        digit = y % 10
        sm += digit
        y = y // 10
    return sm

# count prime digit numbers in list
prime_digit_list = [0] * (MAX_L + 1)

for i in range(2, MAX_L + 1):
    prime_digit_list[i] = prime_digit_list[i - 1]

    if prime[i] and prime[sumdigit(i)]:
        prime_digit_list[i] += 1


# input-output format
t = int(sys.stdin.readline())

while t > 0:
    a, b = map(int, sys.stdin.readline().split())

    if a == 1:
        print(prime_digit_list[b])
    else:
        print(prime_digit_list[b] - prime_digit_list[a-1])
    t -= 1