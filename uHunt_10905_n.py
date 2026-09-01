import sys
from functools import cmp_to_key

def comparator(a,b):
    if a+b > b+a:
        return 1
    else:
        return -1

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    arr_num_temp = sys.stdin.readline().split()
    arr_num = arr_num_temp[:n]

    arr_num.sort(key=cmp_to_key(comparator), reverse = True)

    print(''.join(arr_num))