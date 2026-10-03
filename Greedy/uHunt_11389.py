import sys

while True:

    arr = list(map(int, input().split()))
    n = arr[0]
    d = arr[1]
    r = arr[2]

    if n == 0 and d == 0 and r == 0:
        break

    overitime = 0

    arr_day = list(map(int, sys.stdin.readline().split()))
    arr_night = list(map(int, sys.stdin.readline().split()))

    arr_day.sort()
    arr_night.sort(reverse = True)

    sum_time = []
    for x,y in zip(arr_day, arr_night):
        sum_time.append(x + y)

    for k in sum_time:
        if k > d:
            overitime += (k - d)

    print(overitime * r)
