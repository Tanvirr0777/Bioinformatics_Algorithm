import heapq
import sys
from collections import deque
from functools import cmp_to_key

print("Enter the number of nodes:",end=" ")
V = int(sys.stdin.readline())
nodes = list(range(V))

adj = [[] for _ in range(V)]
edges = []

parent = list(range(V))
size = [1]*V

def comparator(a, b):
    return  a[2] - b[2]

def addEdges(u,v,w):
    adj[u].append((v,w))
    adj[v].append((u,w))
    edges.append((u,v,w))

def display():

    for i in range(len(adj)):
        print(f"{i} : ",end=" ")

        for v,w in adj[i]:
            print(f"{v}({w})",end=" ")

        print()

def bfs():
    src = 0
    l = len(adj)
    visited = [False] * l

    visited[src] = True
    q = deque([src])

    res = []

    while q:
        curr = q.popleft()
        res.append(curr)

        for v,w in adj[curr]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    return res

def dfs():
    src = 0
    l = len(adj)

    visited = [False] * l

    stack = [src]
    res = []

    while stack:
        curr = stack.pop()

        if visited[curr]:
            continue

        visited[curr] = True
        res.append(curr)

        for v,w in adj[curr]:
            if not visited[v]:
                stack.append(v)
    return res

def find(x):

    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    rootx = find(x)
    rooty = find(y)

    if rootx == rooty:
        return False

    if size[rootx] < size[rooty]:
        rootx, rooty = rooty, rootx

    parent[rooty] = rootx

    size[rootx] += size[rootx]

    return True

def kruskal(edges):
    edges = sorted(edges, key=cmp_to_key(comparator))

    mst_cost = 0
    count = 0
    mst = []

    for u,v,w in edges:
        if union(u, v):

            mst_cost += w
            count += 1
            mst.append((u, v,w))

            if count == V-1:
                break

    return mst, mst_cost

def prims():

    visited = [False] * V

    pq = []

    heapq.heappush(pq, (0,-1,0))

    mst = []
    mst_cost = 0

    while pq:

        w,parent,vertex = heapq.heappop(pq)

        if visited[vertex]:
            continue

        visited[vertex] = True

        if parent != -1:
            mst_cost += w
            mst.append((parent, vertex, w))

        for v,weight in adj[vertex]:
            if not visited[v]:
                heapq.heappush(pq, (weight,vertex,v))

    return mst, mst_cost

f = open("input.txt","r")

for line in f:

    a,b,c = line.split()

    u,v,w = int(a),int(b),int(c)

    if u not in nodes or v not in nodes:
        print("Vertex not found")
        break

    addEdges(u,v,w)

display()
print(f"BFS: {bfs()}")
print(f"DFS: {dfs()}")
mst,mst_cost = kruskal(edges)
mstp,mst_costp = prims()

print(f"Minimum spanning tree for kruskal: ")
for u,v,w in mst:
    print(f"{u} -------> {v} with cost: {w}")
print(f"Total cost: {mst_cost}")

print(f"Minimum spanning tree for prims: ")
for u,v,w in mstp:
    print(f"{u} -------> {v} with cost: {w}")
print(f"Total cost: {mst_costp}")

f.close()