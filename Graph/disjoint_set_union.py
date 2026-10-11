
V = 5

parent = list(range(V))

size = [1]*V

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def union(x, y):
    rootx = find(x)
    rooty = find(y)

    if rootx == rooty:
        return False

    if size[rootx] < size[rooty]:
        rootx, rooty = rooty, rootx

    parent[rooty] = rootx

    size[rootx] += size[rooty]

    return True



print("Initial parent:", parent)
print("Initial size:", size)

union(0, 1)
print("After union(0, 1):", parent)

union(1, 2)
print("After union(1, 2):", parent)

union(3, 4)
print("After union(3, 4):", parent)

if find(0) == find(2):
    print("0 and 2 are in the same group")
else:
    print("0 and 2 are in different groups")


if find(0) == find(4):
    print("0 and 4 are in the same group")
else:
    print("0 and 4 are in different groups")
