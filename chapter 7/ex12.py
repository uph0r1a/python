def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


number = int(input(f"Enter a integer greater than 1: "))
numberList = list(range(2, number + 1))

for i in numberList:
    print("Prime" if is_prime(i) else "Composite")
