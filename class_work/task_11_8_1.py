import sys
import mybuiltsfunction


print("Number of element : ",end="")
n = int(sys.stdin.readline())

print("Enter elements of array  : ",end="")
li = list(map(int, sys.stdin.readline().split()))
arr = li[:n]

d = {i:v for i,v in enumerate(arr)}
print("Original array : ",arr)

mybuiltsfunction.merge_sort_asc(arr,0,len(arr)-1)
print("sorted array : ",arr)

print("Enter key to find : ",end="")
target = int(sys.stdin.readline())

res = mybuiltsfunction.binary_search(arr,0,len(arr),target)

pos_original = [key for key,val in d.items() if val == target]


if res == -1:
    print("Number not found")
else:
    print(f"Position in sorted array : {res + 1}")
    print(f"Position in original array : {int(pos_original[0]) + 1}")


