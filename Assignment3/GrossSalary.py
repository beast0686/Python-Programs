def calculate_gross_salary(basic_salary, grade):
    # Calculate HRA (House Rent Allowance)
    hra = 0.20 * basic_salary

    # Calculate DA (Dearness Allowance)
    da = 0.50 * basic_salary

    # Calculate allowance based on grade
    if grade == 'A':
        allowance = 1700
    elif grade == 'B':
        allowance = 1500
    elif grade == 'C':
        allowance = 1300
    else:
        raise ValueError("Invalid grade provided.")

    # Calculate PF (Provident Fund)
    pf = 0.11 * basic_salary

    # Calculate gross salary
    gross_salary = basic_salary + hra + da + allowance - pf

    return gross_salary


# Test the function
basic_salary = float(input("Enter basic salary: "))
grade = input("Enter grade (A/B/C): ")

try:
    gross_salary = calculate_gross_salary(basic_salary, grade)
    print("Gross Salary:", gross_salary)
except ValueError as e:
    print("Error:", e)
