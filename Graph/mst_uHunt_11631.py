import sys

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)

    return parent[x]

def union(x,y,parent,size):

    rootx = find(x,parent)
    rooty = find(y,parent)

    if rootx == rooty:
        return False

    if size[rootx] < size[rooty]:
        rootx,rooty = rooty,rootx

    parent[rooty] = rootx
    size[rootx] += size[rooty]

    return True

def kruskal(V,edges):

    parent = list(range(V))
    size = [1] * V

    edges = sorted(edges, key=lambda edge: edge[2])

    mst_cost = 0
    N = 0

    for u,v,w in edges:

        if union(u,v,parent,size):

            mst_cost += w
            N += 1

            if N == V-1:
                break

    return mst_cost


while True:

    m,n = map(int,sys.stdin.readline().split())

    if m == 0 and n == 0:
        break

    edges = []

    for _ in range(n):
        u, v, l = map(int,sys.stdin.readline().split())
        edges.append((u, v, l))

    prev_cost = sum(l for u, v, l in edges)

    new_cost = kruskal(m,edges)

    print(f"{prev_cost - new_cost}")
    
