from collections import deque

V = 6
adj = [ [] for _ in range(V)]

def addEdges(u,v,w):
    adj[u].append((v,w))
    adj[v].append((u,w))

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


f = open("input.txt", "r")

for line in f:
    a,b,c = line.split()

    u = int(a)
    v = int(b)
    w = int(c)

    addEdges(u,v,w)

display()
bfs = bfs()
print("BFS traversal : ",bfs)
dfs = dfs()
print("DFS traversal : ",dfs)