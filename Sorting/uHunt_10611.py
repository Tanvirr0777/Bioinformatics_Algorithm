import sys


def lower_bound(arr, x, left, right):
    if left >= right:
        return left

    mid = (left + right) // 2

    if arr[mid] >= x:
        return lower_bound(arr, x, left, mid)
    else:
        return lower_bound(arr, x, mid + 1, right)


def upper_bound(arr, x, left, right):
    if left >= right:
        return left

    mid = (left + right) // 2

    if arr[mid] > x:
        return upper_bound(arr, x, left, mid)
    else:
        return upper_bound(arr, x, mid + 1, right)


n = int(sys.stdin.readline())
lady = list(map(int, sys.stdin.readline().split()))

q = int(sys.stdin.readline())
lucu = list(map(int, sys.stdin.readline().split()))

for x in lucu:

    p1 = lower_bound(lady, x, 0, n)

    p2 = upper_bound(lady, x, 0, n)

    if p1 == 0:
        lef = 'X'
    else:
        lef = lady[p1 - 1]

    if p2 == n:
        rigt = 'X'
    else:
        rigt = lady[p2]

    print(lef, rigt)
