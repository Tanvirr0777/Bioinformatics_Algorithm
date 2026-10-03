import sys

f = sys.stdin

for line in f:

   arr_num = list(map(int, line.split()))

   num_head = arr_num[0]
   num_knight = arr_num[1]

   if num_head == 0 and num_knight == 0:
       break

   arr_drg = []
   arr_kght = []

   for i in range(0,num_head):
       x = int(sys.stdin.readline())
       arr_drg.append(x)
   for i in range(0,num_knight):
       y = int(sys.stdin.readline())
       arr_kght.append(y)

   arr_drg.sort()
   arr_kght.sort()
   coin,k,j = 0,0,0

   if len(arr_drg) > len(arr_kght):
       print("Loowater is doomed!")
   else:
      while k < len(arr_drg):
          if j == len(arr_kght):
              break
          if arr_drg[k] <= arr_kght[j]:
              coin += arr_kght[j]
              k += 1
          j += 1

      if k == len(arr_drg) and j <= len(arr_kght):
          print(coin)
      else:
          print("Loowater is doomed!")