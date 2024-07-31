def bold(string):
    def wrapper():
        return "<b>" + string + "</b>"


def italic(string):
    def wrapper():
        return "<i>" + string + "</i>"
    return wrapper()


def underline(string):
    def wrapper():
        return "<u>" + string + "</u>"
    return wrapper()


@bold
@italic
@underline
def say_hello():
    return "Hello"


print(say_hello())
