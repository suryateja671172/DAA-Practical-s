
graph = {}

def BFS(start):
    visited = set()
    queue = []

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for next in graph[node]:
            if next not in visited:
                visited.add(next)
                queue.append(next)


n, e = map(int, input("Enter vertices and edges: ").split())

for i in range(n):
    graph[i] = []

print("Enter edges (u v):")

for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

print("BFS Traversal:")
BFS(start)
