import time
start = time.time()

def factorial_iterative(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter a number: "))
result = factorial_iterative(n)  
print("Factorial =", result)

end = time.time()
print(f"Execution Time: {end-start:.5f} seconds")