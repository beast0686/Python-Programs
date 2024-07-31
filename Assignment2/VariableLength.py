def func1(*args):
    print("Values of the arguments:")
    for arg in args:
        print(arg)


# Test the function with variable arguments
func1(1, 2, 3)
func1('a', 'b', 'c', 'd')
func1(True, False, True, False, True)
