# Fibonacci Series up to 10 terms

def fibo(num):
    n1 = 0
    n2 = 1
    print("Fibonacci series up to 10 terms: ")
    print(n1, end=" ")
    print(n2, end=" ")
    for i in range (2,10):
        new = n1 + n2
        n1 = n2
        n2 = new
        print(new, end=" ")


n = 10
fibo(n)
