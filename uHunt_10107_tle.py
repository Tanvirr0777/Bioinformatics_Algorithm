import sys

inf = float('inf')

def merge(a,l,m,h):

    n1 = m - l + 1
    n2 = h - m

    l_arr = []
    r_arr = []

    for i in range(n1):
        l_arr.append(a[l + i])

    for j in range(n2):
        r_arr.append(a[m + 1 + j])

    l_arr.append(inf)
    r_arr.append(inf)

    i,j = 0,0
    for k in range(l,h+1):
        if l_arr[i] < r_arr[j]:
            a[k] = l_arr[i]
            i += 1
        else:
            a[k] = r_arr[j]
            j +=1

def merge_sort(arr,low,high):
    if low >= high:
        return
    mid = low + (high - low)//2

    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)

    merge(arr,low,mid,high)


f = sys.stdin
med = []
for line in f:
    line = line.strip()
    med.append(int(line))
    merge_sort(med,0,len(med)-1)

    index = len(med) // 2

    if len(med) % 2 != 0:
        print(med[index])
    else:
        print( (med[index-1] + med[index]) // 2 )

