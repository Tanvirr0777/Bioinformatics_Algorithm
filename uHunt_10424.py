import sys

store = "0abcdefghijklmnopqrstuvwxyz"

def total_s(name):
    scr = 0
    global store
    for i in name:
        index = store.find(i.lower())
        if index == -1:
            continue
        else:
         scr += index
    return scr

def sum_digit(n):
     while n > 9:
         s = 0
         while n != 0:
             s += n % 10
             n = n // 10
         n = s
     return n

f = sys.stdin

while True:
   try:
       name1 = next(f).strip()
       name2 = next(f).strip()

       n1s = total_s(name1)
       n2s = total_s(name2)

       n1sum = sum_digit(n1s)
       n2sum = sum_digit(n2s)

       if n1sum > n2sum:
        print( f"{(sum_digit(n2s)/sum_digit(n1s))*100:.2f} %" )
       else:
        print( f"{(sum_digit(n1s)/sum_digit(n2s))*100:.2f} %" )

   except StopIteration:
       break