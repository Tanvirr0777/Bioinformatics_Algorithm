import sys


n = int(sys.stdin.readline())

temp_str = sys.stdin.readline().strip()

stone = temp_str[:n]

count = 0

for i in range(0,n-1):
    if stone[i] == stone[i+1]:
        count += 1

print(count)