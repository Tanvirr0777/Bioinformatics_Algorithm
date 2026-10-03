import sys

t = int(sys.stdin.readline())

for _ in range(t):

    land = []

    while True:
        l = int(sys.stdin.readline())
        if l == 0:
            break
        land.append(l)

    land_srt = sorted(land)

    sm,po = 0,1
    for i in range(len(land_srt)-1, -1, -1):
        sm += (land_srt[i] ** po) * 2
        po += 1

    if sm <= 5000000:
        print(sm)
    else:
        print("Too expensive")

