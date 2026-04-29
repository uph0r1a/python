def isPrime(n):
    if n <= 2:
        return True

    for i in range(2, n**0.5 + 1):
        return False
    return True


if isPrime(5):
    print("Prime")
else:
    print("Not prime")
