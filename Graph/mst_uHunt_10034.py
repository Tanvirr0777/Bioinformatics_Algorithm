import heapq
import sys


adj= []
points = []
edges = []

def distance(x,y):
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5

def operation_edges(adj):

    for i in range(len(points)):
        for j in range(i+1,len(points)):
            w = distance(points[i],points[j])

            heapq.heappush(edges,(w,i,j))
            adj[i].append((j,w))
            adj[j].append((i,w))

def prims(adj):

    visited = [False] * V

    pq = []

    heapq.heappush(pq,(0,-1,0))

    mst_cost = 0

    while pq:
        w,parent,vertex = heapq.heappop(pq)

        if visited[vertex]:
            continue

        visited[vertex] = True

        if parent != -1:
            mst_cost += w

        for v,weight in adj[vertex]:
            if not visited[v]:
                heapq.heappush(pq,(weight,vertex,v))

    return mst_cost



line = sys.stdin.readline()

t = int(line)
for case in range(t):

    while True:
        line = sys.stdin.readline().strip()

        if line:
             V = int(line)
             break

    adj = [[] for _ in range(V)]

    for _ in range(V):
        x,y = sys.stdin.readline().split()
        a,b = float(x),float(y)
        points.append((a,b))

    operation_edges(adj)
    print(f"{prims(adj):.2f}")
    points = []

    if case != t-1:
        print()