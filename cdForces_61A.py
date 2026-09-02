import sys

num1 = sys.stdin.readline().strip()
num2 = sys.stdin.readline().strip()

res = ""

for i,j in zip(num1,num2):
   if i != j:
       res += '1'
   else:
       res += '0'

print(res)