import sys

def partition(a,low,high):

    pivot = a[high]
    i = low - 1

    for j in range(low,high):
        if a[j] <= pivot:
            i += 1
            a[i],a[j] = a[j], a[i]

    a[i+1],a[high] = a[high],a[i+1]

    return i + 1


def quick_sort(ar,low, high):
    if low > high:
        return

    p = partition(ar, low, high)

    quick_sort(ar, low, p - 1)
    quick_sort(ar, p + 1, high)

print("Enter size of array : ",end="")
n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

arr = li[:n]

quick_sort(arr,0, n-1)

print(arr)
