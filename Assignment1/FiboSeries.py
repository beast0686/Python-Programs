def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


# Number of terms in the Fibonacci series
terms = int(input("Enter range: "))

# Display Fibonacci series up to 10 terms
print("Fibonacci series:")
print(fibonacci(terms))
