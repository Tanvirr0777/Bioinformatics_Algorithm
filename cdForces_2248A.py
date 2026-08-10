import sys

t = int(sys.stdin.readline())

for _ in range(t):
    bnumber = sys.stdin.readline().strip()

    lst = list(bnumber)
    zero = lst.index('0')
    one = lst.index('1')

    lst[zero], lst[one] = "", ""

    print(''.join(lst))
