import  sys

inf = float("inf")

def merge(arr, l, m, r):

    n1 = m - l + 1
    n2 = r - m
    l_arr = []
    r_arr = []

    for i in range(0, n1):
        l_arr.append(arr[l + i])

    for j in range(0,n2):
        r_arr.append(arr[m + 1 + j])

    l_arr.append(inf)
    r_arr.append(inf)

    i,j = 0,0
    for k in range(l,r+1):
        if l_arr[i] < r_arr[j]:
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            j += 1


def merge_sort(arr, left, right):

    if left >= right:
        return
    mid = left + (right - left) // 2

    merge_sort(arr,left, mid)
    merge_sort(arr,mid + 1, right)

    merge(arr, left, mid, right)


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
A = a[:n]

low = 0
high = len(A)-1

merge_sort(A, low, high)
print(A)




