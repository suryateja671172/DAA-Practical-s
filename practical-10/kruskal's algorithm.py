
# Kruskal's Algorithm

parent = []

def find(i):
    while parent[i] != i:
        i = parent[i]
    return i


def union(u, v):
    a = find(u)
    b = find(v)

    if a != b:
        parent[b] = a
        return True

    return False


n, e = map(int, input("Enter vertices and edges: ").split())

edges = []

print("Enter edges (u v weight):")

for i in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# Sort edges by weight
edges.sort()

# Initially, each vertex is its own parent
parent = [i for i in range(n)]

cost = 0

print("Edges in Minimum Spanning Tree:")

for w, u, v in edges:
    if union(u, v):
        print(u, "-", v, ":", w)
        cost = cost + w

print("Minimum Cost:", cost)
