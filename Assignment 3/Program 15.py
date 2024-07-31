def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % 2 == 0:
            return False
    return True


def prime_in_range(start, end):
    prime = []
    for i in range(start, end + 1):
        if is_prime(i):
            prime.append(i)
    print(prime)


prime_in_range(1, 10)
