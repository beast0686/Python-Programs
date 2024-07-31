n = 5
for i in range(n):
    print(" "*(n-i), end=" ")
    element = str(11 ** i)
    for char in element:
        print(char, end=" ")
    print()
