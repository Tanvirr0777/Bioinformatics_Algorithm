import sys
from collections import deque


# undirected
def addEdges(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

#directed

def adddirectedEdges(adj,u,v):
    adj[u].append(v)

# cycle detected for undirected graph
def bfs(adj, src, visited):

    q = deque([(src, -1)])
    visited[src] = True

    while q:
        node, parent = q.popleft()

        for x in adj[node]:

            if not visited[x]:
                visited[x] = True
                q.append((x, node))

            elif x != parent:
                return True

    return False

def isCycle(adj):
    l = len(adj)
    visited = [False] * l

    for i in range(l):
        if not visited[i]:
            if bfs(adj, i, visited):
                return True
    return False


#cycle detected in directed graph
def isCycledirected(adj):
    l = len(adj)
    indegree = [0] * l
    visCount = 0

    q = deque()

    for i in range(l):
        for x in adj[i]:
            indegree[x] += 1

    for i in range(l):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        visCount += 1

        for x in adj[node]:
            indegree[x] -= 1

            if indegree[x] == 0:
                q.append(x)

    return visCount != l

V = 4

adj = [[] for _ in range(V)]

f = open("input.txt","r")

for line in f:
    a,b = line.split()

    u = int(a)
    v = int(b)

   # addEdges(adj,u,v)
    adddirectedEdges(adj,u,v)

# res = isCycle(adj)
#
# if res:
#     print("Cycle found")
# else:
#     print("Cycle not found")

if isCycledirected(adj):
    print("Cycle found")
else:
    print("Cycle not found")


