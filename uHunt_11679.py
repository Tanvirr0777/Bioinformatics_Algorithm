import sys

f = sys.stdin

for line in f:
    b,n = line.split()

    b = int(b)
    n = int(n)

    if b == 0 and n == 0:
        break

    rsv_inp = list(map(int,sys.stdin.readline().split()))
    rsv = rsv_inp[:b]

    i = 0
    for i in range(n):
        dev_in = list(map(int,sys.stdin.readline().split()))
        dev = dev_in[:3]

        rsv[dev[0]-1] -= dev[2]
        rsv[dev[1]-1] += dev[2]

    exist = any( bal < 0 for bal in rsv)

    if exist:
        sys.stdout.write("N" + "\n")
    else:
        sys.stdout.write("S" + "\n")
