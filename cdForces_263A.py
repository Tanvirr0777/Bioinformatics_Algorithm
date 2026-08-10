import sys

matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(5)]
r = 0
col = 0
for row in range(5):
    if 1 in matrix[row]:
        col = matrix[row].index(1)
        r = row
        break
r += 1
col += 1
print(abs(3-r) + abs(3-col))