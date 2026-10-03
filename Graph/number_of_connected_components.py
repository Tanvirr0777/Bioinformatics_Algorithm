import sys
from collections import deque

# print("Enter the number of vertex : ",end="")
# V = int(sys.stdin.readline())
V = 8

adj = [ [] for _ in range(V)]

def addEdges(u,v):
    adj[u].append(v)

def displayList():
    for i in range(len(adj)):
        print(f"{i} : ",end="")
        for j in adj[i]:
            print(f"{j} ",end="")
        print()

def bfs(src):
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

def component(src):

    storage = bfs(src)
    print(storage)
    totalComponent = 1

    for i in range(V):

       if i not in storage:
           track = bfs(i)
           print(track)
           storage += track
           totalComponent += 1

    print(totalComponent)


f = open("input.txt","r")

for line in f:
    a,b = line.split()

    u = int(a)
    v = int(b)

    addEdges(u,v)
displayList()

print("Enter the initial source : ",end="")
src = int(sys.stdin.readline())

component(src)