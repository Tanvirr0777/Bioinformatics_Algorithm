import sys

def binary_search(li,l,r,m,key):
    if l > r:
        return -1
    if li[m] == key:
        return m
    if key < li[m]:
        return binary_search(li,l,m-1,(l+m-1)//2,key)
    else:
        return binary_search(li,m+1,r,(m+1+r)//2,key)


print("Enter a list of numbers: ",end="")
arr = list(map(int,sys.stdin.readline().split()))

print("Enter a number to search in list: ",end="")
num = int(sys.stdin.readline())

mid = len(arr)//2
right = len(arr)-1
left = 0

print(arr)

res = binary_search(arr,left,right,mid,num)

if res == -1:
    print("Number not found")
else:
    print(f"Position : {res + 1} , Value : {arr[res]}")