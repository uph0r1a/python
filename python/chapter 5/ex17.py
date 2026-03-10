def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print("Enter a number: ", end="")
number = int(input())

if is_prime(number):
    print("Prime")
else:
    print("Not prime")
