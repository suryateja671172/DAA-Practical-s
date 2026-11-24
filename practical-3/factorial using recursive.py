import time
start = time.time()

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
     return n * factorial_recursive(n - 1)

n = int(input("Enter a number: "))

result = factorial_recursive(n)
print("Factorial =", result)

end = time.time()
print(f"Execution Time: {end-start:.5f} seconds")