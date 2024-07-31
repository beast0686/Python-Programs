age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to drive")
elif 0 <= age < 18:
    print("Not eligible to drive")
else:
    print("Invalid input")
