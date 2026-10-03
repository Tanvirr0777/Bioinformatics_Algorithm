import sys
from collections import deque

case = 1


def addEdges(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def bfs(adj, src, ttl):
    l = len(adj)
    visited = [False] * l
    dist = [0] * l

    visited[src] = True

    q = deque()
    q.append(src)

    res = []

    while q:
        curr = q.popleft()
        res.append(curr)

        for x in adj[curr]:
            if not visited[x] and dist[curr] + 1 <= ttl:
                visited[x] = True
                dist[x] = dist[curr] + 1
                q.append(x)

    return len(adj) - len(res)


def allbfs(adj, src, ttl, rev_index):
    global case

    for x,y in zip(src,ttl):
        s = 0
        if isinstance(x,tuple) and len(x) > 1 and x[0] == -1:
            res = len(adj)
            s = x[1]
        else:
            res = bfs(adj, x, y)
            s = rev_index[x]

        global case
        print( f"Case {case}: {res} nodes not reachable from node {s} with TTL = {y}.")

        case += 1


for line in sys.stdin:

    line = line.strip()

    if not line:
        continue

    node_number = int(line)

    if node_number == 0:
        break

    index = {}

    edges = []

    while len(edges) < 2 * node_number:

        line = sys.stdin.readline().strip()

        if not line:
            continue

        edge = list(map(int, line.split()))
        edges += edge

    queries = []

    while True:
        line = sys.stdin.readline().strip()

        if not line:
            continue

        query = list(map(int, line.split()))

        if query[-1] == 0 and query[-2] == 0:

            query = query[:-2]
            queries += query

            break

        queries += query

    for x in edges:
        if x not in index:
            index[x] = len(index)

    adj = [[] for _ in range(len(index))]

    for k in range(0, len(edges) - 1, 2):

        a = edges[k]
        b = edges[k + 1]

        u = index[a]
        v = index[b]

        addEdges(adj, u, v)

    src = []

    for i in range(0, len(queries), 2):
        q = queries[i]

        if q not in index:
            src.append((-1,q))
        else:
            src.append(index[q])

    ttl = []
    for j in range(1, len(queries), 2):
        a = queries[j]
        ttl.append(a)

    rev_index = {v: k for k, v in index.items()}

    allbfs(adj, src, ttl, rev_index)