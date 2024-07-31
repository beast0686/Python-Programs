def fibo(n):
    n1 = 0
    n2 = 1
    print(n1, end=" ")
    print(n2, end=" ")
    for i in range(2, n):
        new = n1 + n2
        n1 = n2
        n2 = new
        print(new, end=" ")


fibo(10)