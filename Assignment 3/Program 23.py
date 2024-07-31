def func1(*args):
    for arg in args:
        print(arg, end=" ")


sample = ["hello", "world", 123, True]
func1(sample)