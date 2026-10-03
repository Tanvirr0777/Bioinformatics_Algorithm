from collections import deque


def addEdges(adj,u,v):
   adj[u].append(v)
   adj[v].append(u)

def display(adj):

    for i in range(len(adj)):
        print(f"{i} : ",end=" ")
        for j in adj[i]:
            print(j,end=" ")
        print()

def bfs(adj):
    src = 0

    l = len(adj)
    visited = [False] * l

    visited[src] = True

    q = deque()
    q.append(src)

    res = []

    while q:
        curr = q.popleft()
        res.append(curr)

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
    return res


def dfs(adj):
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

        for x in adj[curr]:
            if not visited[x]:
                stack.append(x)

    return res


# vertices number
V = 5
adj = [ [] for _ in range(V) ]

f = open("input.txt","r")

for line in f:
    a,b = line.split()

    u = int(a)
    v = int(b)

    addEdges(adj,u,v)
f.close()

display(adj)

print("BFS traversal : ")
res = bfs(adj)
print(res)
print("DFS traversal : ")
resdfs = dfs(adj)
print(resdfs)