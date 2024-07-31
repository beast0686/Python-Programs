def outer_func():
    def inner_func():
        print("Inner function")
    return inner_func()


outer_func()
