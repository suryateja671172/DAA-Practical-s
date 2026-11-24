
graph = {}

def DFS(node, visited):
    visited.add(node)
    print(node, end=" ")

    for next in graph[node]:
        if next not in visited:
            DFS(next, visited)


n, e = map(int, input("Enter vertices and edges: ").split())

for i in range(n):
    graph[i] = []

print("Enter edges (u v):")

for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

print("DFS Traversal:")
DFS(start, set())
