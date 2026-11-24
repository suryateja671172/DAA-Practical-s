
import time
from itertools import permutations

n = int(input("Enter number of cities: "))

print("Enter cost matrix:")

a = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

minCost = 99999

start = time.time()

# Generate all possible paths
p = list(range(1, n))

for path in permutations(p):
    cost = a[0][path[0]]

    for i in range(n - 2):
        cost = cost + a[path[i]][path[i + 1]]

    cost = cost + a[path[n - 2]][0]

    if cost < minCost:
        minCost = cost

end = time.time()

print("Minimum Travelling Cost =", minCost)
print("Execution Time =", end - start, "seconds")
