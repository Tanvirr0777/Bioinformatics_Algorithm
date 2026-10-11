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


def heap_sort(arr,n):
    i = n // 2 - 1

    while i >= 0:
        max_heapify(arr, i, n) # for ascending use max_heap
        i -= 1

    for j in range(n-1,0,-1):
        arr[j],arr[0] = arr[0],arr[j]
        max_heapify(arr,0,j) # for descending use max_heap


arr = list(map(int, sys.stdin.readline().split()))

n = len(arr)

print(arr)
heap_sort(arr,n)

print(arr)