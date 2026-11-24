# Chain Matrix Multiplication using Dynamic Programming

n = int(input("Enter number of matrices: "))
p = []
for i in range(n + 1):
    x = int(input("Enter dimension: "))
    p.append(x)

m = [[0 for j in range(n)] for i in range(n)]

for length in range(2, n + 1):

    for i in range(n - length + 1):

        j = i + length - 1
        m[i][j] = 999999

        for k in range(i, j):

            cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j]

            if cost < m[i][j]:
                m[i][j] = cost

print("Minimum number of multiplications:", m[0][n - 1])