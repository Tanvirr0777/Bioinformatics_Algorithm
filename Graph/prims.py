import heapq
from collections import deque


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

        for x,w in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
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

        for x,w in adj[curr]:
            if not visited[x]:
                stack.append(x)
    return res

V = 7
adj = [ [] for _ in range(V)]

def addEdges(u,v,w):
    adj[u].append((v,w))
    adj[v].append((u,w))

def prim():

    visited = [False] * V

    pq = []   # Heap: (weight, parent, vertex)

    heapq.heappush(pq, (0, -1, 0))

    mst = []
    mst_cost = 0

    while pq:

        w, parent, vertex = heapq.heappop(pq)

        if visited[vertex]:
            continue

        visited[vertex] = True

        if parent != -1:
            mst.append((parent, vertex, w))    # Store as (parent, vertex, weight)
            mst_cost += w

        for v, weight in adj[vertex]:
            if not visited[v]:
                heapq.heappush(pq, (weight, vertex, v))

    return mst,mst_cost

f = open("input.txt", "r")

for line in f:
    a,b,c = line.split()

    u = int(a)
    v = int(b)
    w = int(c)

    addEdges(u,v,w)

display()

print("Minimum spanning Tree : ")
mst,mst_cost = prim()
for x in mst:
    print(f"{x[0]} ---> {x[1]} with cost :{x[2]}")

print(f"MST cost: {mst_cost}")