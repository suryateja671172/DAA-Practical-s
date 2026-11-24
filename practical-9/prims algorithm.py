graph = {}
n = int(input("Enter number of vertices: "))
for i in range(n):
    v = input("Enter vertex: ")
    graph[v] = []
e = int(input("Enter number of edges: "))
for i in range(e):
    u, v, w = input("Enter edge and weight (A B 10): ").split()
    w = int(w)
    graph[u].append((v, w))
    graph[v].append((u, w))
def prim(start):
    visited = {start}
    cost = 0
    while len(visited) < n:
        minimum = float('inf')
        edge = None
        for u in visited:
            for v, w in graph[u]:
                if v not in visited and w < minimum:
                    minimum = w
                    edge = (u, v)
        if edge is None:
            print("Graph is disconnected!")
            return
        u, v = edge
        print(u, "--", v, ":", minimum)
        visited.add(v)
        cost += minimum
    print("Minimum Cost:", cost)
start = input("Enter starting vertex: ")
if start in graph:
    print("Minimum Spanning Tree:")
    prim(start)
else:
    print("Invalid starting vertex!")
