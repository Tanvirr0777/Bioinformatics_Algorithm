import sys

def min_heapify(arr,i,n):

    l = 2*i + 1
    r = 2*i + 2
    min = i

    if l < n and arr[l] < arr[min]:
        min = l
    if r < n and arr[r] < arr[min]:
        min = r

    if min != i:
         arr[i], arr[min] = arr[min], arr[i]
         min_heapify(arr,min,n)


arr = list(map(int, sys.stdin.readline().split()))

n = len(arr)

i = n//2 -1

print(arr)

while i >= 0:
    min_heapify(arr,i,n)
    i -= 1

print(arr)