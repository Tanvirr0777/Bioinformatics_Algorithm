import sys
import re
from functools import reduce

s = sys.stdin.readline()

temp = re.findall(r'\d+',s)

res = []
mx = float('-Inf')

for i in temp:
    res.append(int(i))

res.sort()
res = reduce(lambda x,y:str(x)+"+"+str(y), res)
print(res)