def multiplication_table(number):
    print(f"Multiplication table of {number}: ")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


# Input number from the user
num = int(input("Enter a number to print its multiplication table: "))

# Call the function to print the multiplication table
multiplication_table(num)
