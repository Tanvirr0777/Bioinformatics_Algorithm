import sys


hate = "I hate that"
lst_hate = "I hate it"

love = "I love that"
last_love = "I love it"


n = int(sys.stdin.readline())

res = ""

if n == 1:
    print("I hate it")
elif n == 2:
    print("I hate that I love it")

else:
    i = 1
    while i <= n-1:
        if i % 2 == 0:
            res += " " + love
        else:
            res += " " + hate
        i += 1
    if n % 2 == 0:
        res += " " + last_love
    else:
        res += " " + lst_hate

    print(res.strip())