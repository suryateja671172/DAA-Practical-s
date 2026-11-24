
import time

n = int(input("Enter vertices: "))

print("Enter matrix (999 for no edge):")

a = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

start = time.time()

# Floyd-Warshall Algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][k] + a[k][j] < a[i][j]:
                a[i][j] = a[i][k] + a[k][j]

end = time.time()

print("Shortest Distance Matrix:")

for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()

print("Execution Time:", end - start, "seconds")
