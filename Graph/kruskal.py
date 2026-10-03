from functools import cmp_to_key

V = 6
adj = [ [] for _ in range(V)]
edges = []

parent = list(range(V))
size = [1] * V

def comparator(a, b):
    return a[2] - b[2]

def addEdges(u,v,w):
    adj[u].append((v,w))
    adj[v].append((u,w))
    edges.append((u,v,w))

def display():
    for i in range(len(adj)):
        print(f"{i} : ",end=" ")

        for v,w in adj[i]:
            print(f"{v}({w})",end=" ")
        print()

def find(x):

    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):

    rootx = find(x)
    rooty = find(y)

    if rootx == rooty:
        return False

    if size[rootx] < size[rooty]:
        rootx, rooty = rooty, rootx

    parent[rooty] = rootx

    size[rootx] += rooty

    return True

def kruskal(V,edges):

    edges = sorted(edges, key = cmp_to_key(comparator))

    mst_cost = 0
    edges_used = 0
    mst = []

    for x,y,w in edges:
        if union(x,y):

            mst.append((x,y,w))

            mst_cost += w
            edges_used += 1

            if edges_used == V-1:
                break

    return mst,mst_cost


f = open("input.txt", "r")

for line in f:
    a,b,c = line.split()

    u = int(a)
    v = int(b)
    w = int(c)

    addEdges(u,v,w)

display()

print("Minimum spanning Tree : ")
mst,mst_cost = kruskal(V,edges)
for x in mst:
    print(f"{x[0]} ---> {x[1]} with cost :{x[2]}")

print(f"MST cost: {mst_cost}")
