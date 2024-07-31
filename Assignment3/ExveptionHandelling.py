def divide_numbers(x, y):
    try:
        result = x / y
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print("An error occurred:", e)


# Test the function with different inputs
try:
    divide_numbers(10, 2)  # Normal division
    divide_numbers(10, 0)  # Division by zero
    divide_numbers("10", 2)  # Invalid operation (TypeError)
except:
    print("An error occurred during function execution.")
