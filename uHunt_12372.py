import sys

t = int(sys.stdin.readline())

for i in range(t):
    l,w,h = map(int, sys.stdin.readline().split())
    if 0 < l < 21 and 0 < w < 21 and 0 < h < 21:
        print(f"Case {i+1}: good")
    else:
        print(f"Case {i+1}: bad")