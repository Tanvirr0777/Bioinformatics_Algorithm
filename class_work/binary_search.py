import sys

import mybuiltsfunction

def binary_search(li,l,r,key):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if li[m] == key:
        return m
    if key > li[m]:
        return binary_search(li,l,m-1,key)
    else:
        return binary_search(li,m+1,r,key)


print("Enter a list of numbers: ",end="")
arr = list(map(int,sys.stdin.readline().split()))

print("Enter a number to search in list: ",end="")
num = int(sys.stdin.readline())

right = len(arr)-1
left = 0

mybuiltsfunction.merge_sort_desc(arr,left, right)
print(arr)

res = binary_search(arr,left,right,num)

if res == -1:
    print("Number not found")
else:
    print(f"Position : {res + 1} , Value : {arr[res]}")