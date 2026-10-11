V, E = map(int, input().split())
edges = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

src = int(input())

dist = [float('inf')] * V
dist[src] = 0

for _ in range(V - 1):
    changed = False

    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            changed = True

    if not changed:
        break

negative_cycle = False

for u, v, w in edges:
    if dist[u] != float('inf') and dist[u] + w < dist[v]:
        negative_cycle = True
        break

if negative_cycle:
    print("Negative cycle detected")
else:
    for i in range(V):
        print(i, ":", dist[i] if dist[i] != float('inf') else "INF")