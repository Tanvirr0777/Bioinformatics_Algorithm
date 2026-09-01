import sys

def max_heapify(arr,i,n):

    l = 2*i + 1
    r = 2*i + 2
    largest = i

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
         arr[i], arr[largest] = arr[largest], arr[i]
         max_heapify(arr,largest,n)


arr = list(map(int, sys.stdin.readline().split()))

n = len(arr)

i = n//2 -1

print(arr)

while i >= 0:
    max_heapify(arr,i,n)
    i -= 1

print(arr)