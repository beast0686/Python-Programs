def display_student(name, age):
    print("Student Name:", name)
    print("Student Age:", age)


# Assigning a new name to the existing function
show_student = display_student

# Call the function using the new name
show_student("Aman", 20)
