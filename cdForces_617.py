import sys
from math import ceil

p = int(sys.stdin.readline())

steps = [1,2,3,4,5]

s = list(map(lambda x: ceil(p / x) , steps))

print(min(s))