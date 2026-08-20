import sys

def marbel_search(arr,l,r,key,index):
    if l > r:
        return index

    mid = l + (r - l) // 2

    if arr[mid] == key:
        index.append(mid)

    if arr[mid] >= key:
        return marbel_search(arr,l,mid-1,key,index)
    else:
        return marbel_search(arr,mid+1,r,key,index)


f = sys.stdin

case = 0

for line in f:
    case += 1
    n,q = map(int,line.split())

    if n == 0 and q == 0:
        break

    marbel_temp = []
    for i in range(0,n):
        m = int(f.readline())
        marbel_temp.append(m)

    query = []
    for j in range(0,q):
        qu = int(f.readline())
        query.append(qu)

    marbel =  sorted(marbel_temp)
    print(f"CASE# {case}:")

    for value in query:
        index = []
        position = marbel_search(marbel,0,n-1,value,index)

        position.sort()

        if len(position) > 0:
            print(f"{value} found at {position[0]+1}")
        else:
            print(f"{value} not found")

