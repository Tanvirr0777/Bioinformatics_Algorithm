from collections import deque

V = 6
adj = [[] for _ in range(V)]

def topologicalsort():

    topsort = []
    l = len(adj)
    indegree = [0] * l

    q = deque()

    for i in range(V):
        for x in adj[i]:
            indegree[x] += 1

    for i in range(V):
     if indegree[i] == 0:
         q.append(i)

    while q:
        node = q.popleft()
        topsort.append(node)

        for x in adj[node]:
            indegree[x] -= 1

            if indegree[x] == 0:
                q.append(x)

    return topsort

f = open("input.txt","r")

for line in f:
    a,b = line.split()

    u = int(a)
    v = int(b)

    adj[u].append(v)

res = topologicalsort()
print(res)



