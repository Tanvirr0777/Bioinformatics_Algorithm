import sys

a,b = map(int, sys.stdin.readline().split())

year = 0

while True:
    year += 1
    a *= 3
    b *= 2
    if a > b:
        break

print(year)

'''
also solve using logarithmic expansion

   a * 3^n   >    b * 2^n
   
   n = [log(b/a,3/2)] + 1
   n = floor(n)

'''