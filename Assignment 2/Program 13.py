import sys


def print_args():
    for i, arg in enumerate(sys.argv):
        print(f"{i}: {arg}")


print_args()
