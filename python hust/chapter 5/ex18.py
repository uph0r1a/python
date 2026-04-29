def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


for i in range(1, 101):
    if is_prime(i):
        print(i)
