def detect_local_variables():
    # Local variables
    var1 = 1
    var2 = 'hello'
    var3 = [1, 2, 3]

    local_vars = locals()
    return len(local_vars)


# Call the function and print the number of local variables
num_locals = detect_local_variables()
print("Number of local variables:", num_locals)
