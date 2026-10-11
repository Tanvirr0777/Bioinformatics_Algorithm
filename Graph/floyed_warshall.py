V, E = map(int, input().split())
INF = float('inf')

dist = [[INF] * V for _ in range(V)]

for i in range(V):
    dist[i][i] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    dist[u][v] = min(dist[u][v], w)

    # For an undirected graph, uncomment:
    # dist[v][u] = min(dist[v][u], w)

for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][k] != INF and dist[k][j] != INF:
                dist[i][j] = min( dist[i][j], dist[i][k] + dist[k][j]
                )

if any(dist[i][i] < 0 for i in range(V)):
    print("Negative cycle detected")
else:
    for row in dist:
        print(*[x if x != INF else "INF" for x in row])