# Calculate sum of all numbers drom 1 to a given number

n = int(input("Enter range limit: "))
sum = 0
for i in range(n):
    sum = sum + i
print("Sum:", sum)