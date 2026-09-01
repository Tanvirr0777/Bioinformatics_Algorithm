import heapq
import sys

mx_heap = []
min_heap = []

def root_transfer(len_min,len_mx):
    while True:
        if abs(len(min_heap) - len(mx_heap)) == 0 or abs(len(min_heap) - len(mx_heap)) == 1:
          break

        if len_min > len_mx:
            x = heapq.heappop(min_heap)
            heapq.heappush(mx_heap, -x)
        else:
            y = heapq.heappop(mx_heap)
            heapq.heappush(min_heap, -y)

f = sys.stdin

for line in f:
    n = int(line)

    if len(mx_heap) == 0 or n <= -mx_heap[0]:
        heapq.heappush(mx_heap, -n)
    else:
        heapq.heappush(min_heap, n)

    len_mx_heap = len(mx_heap)
    len_min_heap = len(min_heap)

    if len_min_heap == 0:
        print(-mx_heap[0])

    elif abs(len_min_heap - len_mx_heap) > 1:
            root_transfer(len_min_heap,len_mx_heap)

    len_mx_heap = len(mx_heap)
    len_min_heap = len(min_heap)

    if len_mx_heap == len_min_heap:
        pos = -mx_heap[0]
        print( (pos + min_heap[0]) // 2 )

    else:
        if len_mx_heap - len_min_heap == 1 and len_min_heap != 0:
                print(-mx_heap[0])
        if len_min_heap - len_mx_heap == 1 and len_mx_heap != 0:
            print(min_heap[0])


