import sys

t = int(sys.stdin.readline())

for i in range(t):
    a,b,c = map(int, sys.stdin.readline().split())
    if b < a < c or c < a < b:
     print(f"Case {i+1}:" ,a)
    elif a < b < c or c < b < a:
        print(f"Case {i + 1}:", b)
    else:
        print(f"Case {i+1}:", c)