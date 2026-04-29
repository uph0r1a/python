def evenOdd(n):
    print(f"{n} is {"Even" if n % 2 == 0 else "Odd"}")


def multiple4(n):
    print(f"{n} is {"" if n % 4 == 0 else "not "}a multiple of 4")


num = int(input("Enter number 1: "))
check = int(input("Enter number 2: "))

evenOdd(num)
evenOdd(check)
multiple4(num)
multiple4(check)

print(f"{num} does {"" if num % check == 0 else "not "}divide evenly by {check}")
