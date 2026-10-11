import sys
from collections import deque


def bfs(adj,src,dst):
    l = len(adj)
    visited = [False] * l
    parent = [-1] * l

    visited[src] = True

    q = deque([src])

    while q:
        curr = q.popleft()

        if curr == dst:
            break

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                parent[x] = curr
                q.append(x)

    if not visited[dst]:
        return []

    path = []
    curr = dst

    while curr != -1:
        path.append(curr)
        curr = parent[curr]

    return path[::-1]

while True:
    line = sys.stdin.readline()

    if not line:
        break

    n = int(line)

    adj = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        id, child = sys.stdin.readline().split("-")

        node = int(id)
        if child.strip():
            adj_list = list(map(int, child.split(",")))
            adj[node] = adj_list
        else:
            adj[node] = []

    m = int(sys.stdin.readline())
    routes = []
    for _ in range(m):
        a, b = sys.stdin.readline().split()
        src = int(a)
        dst = int(b)
        routes.append((src, dst))

    print("-" * 5)
    for x in routes:
        res = bfs(adj, x[0], x[1])
        if res:
            print(" ".join(map(str, res)))
        else:
            print("connection impossible")