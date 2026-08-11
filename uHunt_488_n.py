import sys

t = int(sys.stdin.readline())

for i in range(t):
    line = sys.stdin.readline().strip()
    while line == "":
        line = sys.stdin.readline().strip()
    a = int(line)

    line = sys.stdin.readline().strip()
    while line == "":
        line = sys.stdin.readline().strip()
    f = int(line)


    for j in list(range(1, a + 1)) + list(range(a-1,0,-1)):
        for k in range(j):
            print(j, end="")
        print()


    if i != t - 1:
        print()