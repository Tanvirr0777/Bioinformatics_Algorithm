import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):

    n = int(sys.stdin.readline())

    total_s = []
    for i in range(0,n):
        s = int(sys.stdin.readline())
        total_s.append(s)

    l = math.factorial(n) // ( math.factorial(n-2) * 2 )

    res = []
    j,k,c = 0,1,0
    while True:
        c += 1
        if k == n:
            j += 1
            k = j + 1
            continue
        res.append(total_s[j] - total_s[k])
        k += 1

        if len(res) == l:
            break
    sys.stdout.write(str(c)+" "+str(max(res)) + "\n")







'''for _ in range(t):

    n = int(sys.stdin.readline())

    total_s = []
    for i in range(0,n):
        s = int(sys.stdin.readline())
        total_s.append(s)

    res = []
    for i in range(0,n):
        for j in range(i+1,n):
            res.append(total_s[i] - total_s[j])

    print(max(res))
print()'''


