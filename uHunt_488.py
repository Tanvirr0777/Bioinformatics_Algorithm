import sys

def triangleprint(a):
    for j in list(range(1, a + 1)) + list(range(a-1,0,-1)):
        for l in range(j):
            print(j, end="")
        print()

t = int(sys.stdin.readline())

i = 0
for i in range(t):
    line = sys.stdin.readline().strip()
    while line == "":
        line = sys.stdin.readline().strip()
    a = int(line)

    line = sys.stdin.readline().strip()
    while line == "":
        line = sys.stdin.readline().strip()
    f = int(line)

    for k in range(0,f):
        triangleprint(a)
        if k != f-1 :
         print()

    if i!= t-1 :
        print()
