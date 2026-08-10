import sys

def score(sr):
    sm = 0
    init = 0
    for char in sr:
        if char == "O":
            init += 1
            sm += init
        else:
            init = 0
    return sm

t = int(sys.stdin.readline())

for _ in range(t):
    n = sys.stdin.readline().strip()
    n = n.upper()
    print(score(n))
