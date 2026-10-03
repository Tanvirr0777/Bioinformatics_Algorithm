import sys
from collections import deque


def addEdges(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def bfs(adj, src, dest):

    l = len(adj)
    visited = [False] * l
    parents = [-1] * l

    visited[src] = True

    q = deque()
    q.append(src)

    while q:
        curr = q.popleft()

        if curr == dest:
            break

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                parents[x] = curr
                q.append(x)

    if not visited[dest]:
        return []

    res = []
    curr = dest

    while curr != -1:
        res.append(curr)
        curr = parents[curr]

    res.reverse()

    return res


first = True
while True:

    line = sys.stdin.readline()

    if not line:
        break

    line = line.strip()

    if not line:
        continue

    city = int(line)

    cities = []

    for i in range(city):

        line = sys.stdin.readline().strip()

        u, v = line.split()

        cities.append(u)
        cities.append(v)

    line = sys.stdin.readline().strip()

    src, dest = line.split()

    index = {}

    for x in cities:
        if x not in index:
            index[x] = len(index)

    if not first:
        print()

    first = False

    if src not in index or dest not in index:
        print("No route")
        continue

    adj = [[] for i in range(len(index))]

    for k in range(0, len(cities) - 1, 2):

        a = cities[k]
        b = cities[k + 1]

        u = index[a]
        v = index[b]

        addEdges(adj, u, v)

    rev_index = {v: k for k, v in index.items()}
    res = bfs(adj, index[src], index[dest])

    if res:
        for i in range(0, len(res) - 1):
            a = rev_index[res[i]]
            b = rev_index[res[i + 1]]

            print(a, b)
    else:
        print("No route")
