import sys

segments = {
    '0': [1, 1, 1, 0, 1, 1, 1],
    '1': [0, 0, 1, 0, 0, 1, 0],
    '2': [1, 0, 1, 1, 1, 0, 1],
    '3': [1, 0, 1, 1, 0, 1, 1],
    '4': [0, 1, 1, 1, 0, 1, 0],
    '5': [1, 1, 0, 1, 0, 1, 1],
    '6': [1, 1, 0, 1, 1, 1, 1],
    '7': [1, 0, 1, 0, 0, 1, 0],
    '8': [1, 1, 1, 1, 1, 1, 1],
    '9': [1, 1, 1, 1, 0, 1, 1]
}

for line in sys.stdin:
    s, n = line.split()

    if s == '0' and n == '0':
        break

    s = int(s)
    rows = 2 * s + 3

    for r in range(rows):
        parts = []

        for d in n:
            seg = segments[d]

            if r == 0:
                parts.append(
                    " " + ("-" * s if seg[0] else " " * s) + " "
                )

            elif 1 <= r <= s:
                parts.append(
                    ("|" if seg[1] else " ")
                    + (" " * s)
                    + ("|" if seg[2] else " ")
                )

            elif r == s + 1:
                parts.append(
                    " " + ("-" * s if seg[3] else " " * s) + " "
                )

            elif s + 2 <= r <= 2 * s + 1:
                parts.append(
                    ("|" if seg[4] else " ")
                    + (" " * s)
                    + ("|" if seg[5] else " ")
                )

            else:
                parts.append(
                    " " + ("-" * s if seg[6] else " " * s) + " "
                )

        print(" ".join(parts))

    print()


"""
import sys
from math import ceil


def display(s,num):
    row = 2 * s + 3
    col = s + 2
    mid = ceil(row / 2)

    for i in range(1, row + 1):
        for j in range(1, col + 1):

            if num == 0 and i == mid:
                continue
            if num == 1 and j > 1:
                continue
            if num == 2 and (i < mid and j == 1 or i > mid and j == col):
                print(" ",end="")
                continue
            if num == 3 and j == 1:
                continue
            if num == 4 and (i == 1 or i > mid and j == 1 or i == row) :
                print(" ",end="")
                continue
            if num == 5 and (i < mid and j == col or i > mid and j == 1):
                print(" ",end="")
                continue
            if num == 6 and i < mid and j == col:
                continue
            if num == 7 and (j == 1 or i == mid or i == row):
                print(" ",end="")
                continue
            if num == 9 and (i > mid and j == 1):
                print(" ",end="")
                continue

            if i == 1 or i == mid or i == row:
                if j == 1 or j == col:
                    print(" ", end="")
                else:
                    print("-", end="")
            elif j == 1 or j == col:
                print("|", end="")
            else:
                print(" ", end="")
        print()
    print(end="")


while True:
    n, number = map(int, sys.stdin.readline().split())
    if n == 0 and number == 0:
        break
    digit = list(map(int,str(number)))
    for k in digit:
        display(n,k)
"""