import sys

t = int(sys.stdin.readline())

i = 0
while i < t:

    s,d = map(int,sys.stdin.readline().split())

    x = (s + d) // 2
    y = (s - d) // 2

    if x < 0 or y < 0 or s < d or (s+d)%2 !=0:
        print("impossible")
    else:
        print(x,y)

    i += 1

'''
import sys
from sympy import symbols,Eq,solve

t = int(sys.stdin.readline())

i = 0
while i < t:

    s,d = map(int,sys.stdin.readline().split())

    x,y = symbols('x y')

    eq1 = Eq(x + y,s)
    eq2 = Eq(x - y,d)

    res = solve((eq1,eq2),(x,y))

    a = res[x]
    b = res[y]

    if a < 0 or b < 0:
        print("impossible")
    else:
        print(a,b)

    i += 1

'''