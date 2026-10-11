import heapq

V, E = map(int, input().split())
adj = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))  # Undirected graph

src = int(input())

dist = [float('inf')] * V
dist[src] = 0
pq = [(0, src)]

while pq:
    d, u = heapq.heappop(pq)

    if d != dist[u]:
        continue

    for v, w in adj[u]:
        new_dist = d + w

        if new_dist < dist[v]:
            dist[v] = new_dist
            heapq.heappush(pq, (new_dist, v))

for i in range(V):
    print(i, ":", dist[i] if dist[i] != float('inf') else "INF")