def greet(name, greeting="Hello"):
    """
    Function to greet a person with a default greeting.

    Parameters:
        name (str): The name of the person.
        greeting (str): The greeting to be used. Default is "Hello".
    """
    print(f"{greeting}, {name}!")


# Calling the function with both parameters provided
greet("Alice", "Hi")

# Calling the function with only the name parameter provided, using default greeting
greet("Bob")

# Calling the function with no parameters provided, using both default name and greeting
greet()
