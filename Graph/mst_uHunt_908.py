import sys

def addEdges(adj, edges, u, v, w):
    adj[u].append((v, w))
    adj[v].append((u, w))
    edges.append((u, v, w))


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)

    return parent[x]


def union(x, y, parent, size):
    rootx = find(x, parent)
    rooty = find(y, parent)

    if rootx == rooty:
        return False

    if size[rootx] < size[rooty]:
        rootx, rooty = rooty, rootx

    parent[rooty] = rootx
    size[rootx] += size[rooty]

    return True


def kruskal(N, edges):
    parent = list(range(N + 1))
    size = [1] * (N + 1)

    edges = sorted(edges, key=lambda edge: edge[2])

    mst_cost = 0
    edges_used = 0

    for u, v, w in edges:
        if union(u, v, parent, size):
            mst_cost += w
            edges_used += 1

            if edges_used == N - 1:
                break

    return mst_cost

res = []

while True:
    line = sys.stdin.readline()

    if not line:
        break

    if line.strip() == "":
        continue

    N = int(line)

    prev_edges = []
    for _ in range(N - 1):
        u, v, w = map(int, sys.stdin.readline().split())
        prev_edges.append((u, v, w))

    cost_prev = sum(w for u, v, w in prev_edges)

    K = int(sys.stdin.readline())
    new_edges = []

    for _ in range(K):
        u, v, w = map(int, sys.stdin.readline().split())
        new_edges.append((u, v, w))

    M = int(sys.stdin.readline())
    original_edges = []

    for _ in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        original_edges.append((u, v, w))

    total_edges = original_edges + new_edges
    cost_total = kruskal(N, total_edges)

    res.append(f"{cost_prev}\n{cost_total}")

print("\n\n".join(res))