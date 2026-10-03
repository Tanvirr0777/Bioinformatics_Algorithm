import sys

def numberseq(num):
    seq = ""
    for s in range(1,num+1):
        seq += str(s)

    freq = [0] * 10

    for char in seq:
        if freq[int(char)] == 0:
            freq[int(char)] = 1
        else:
            freq[int(char)] += 1
    print(" ".join(map(str,freq)))

n = int(sys.stdin.readline())

for _ in range(n):

    number = int(sys.stdin.readline())
    numberseq(number)