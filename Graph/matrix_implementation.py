from collections import deque

def bfs(adj):
    l = len(adj)
    visited = [False] * l
    src = 4

    q = deque()

    visited[src] = True
    q.append(src)

    res = []

    while q:
        curr = q.popleft()
        res.append(curr)

        for i in range(l):
            if adj[curr][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)

    return res


vertices = 5
adj = [[0] * vertices for _ in range(vertices)]

f = open("input.txt", "r")

for line in f:
    a, b = line.split()

    u = int(a)
    v = int(b)

    # Add undirected edge
    adj[u][v] = 1
    adj[v][u] = 1

f.close()

for i in range(len(adj)):
    print(f"{i} : ", end=" ")
    for j in adj[i]:
        print(j, end=" ")
    print()

print("BFS traversal:")
res = bfs(adj)
print(res)