import heapq
import sys

mx_heap = []   # max heap
min_heap = []  # min heap

for line in sys.stdin:
    x = int(line)

    # Add x
    if not mx_heap or x <= -mx_heap[0]:
        heapq.heappush(mx_heap, -x)
    else:
        heapq.heappush(min_heap, x)

    # Balance heaps
    if len(mx_heap) > len(min_heap) + 1:
        x = -heapq.heappop(mx_heap)
        heapq.heappush(min_heap, x)

    elif len(min_heap) > len(mx_heap):
        x = heapq.heappop(min_heap)
        heapq.heappush(mx_heap, -x)

    # Find median
    if len(mx_heap) == len(min_heap):
        median = (-mx_heap[0] + min_heap[0]) // 2
    else:
        median = -mx_heap[0]

    print(median)
