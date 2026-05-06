def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    print(result, end=" ")
    return result


try:
    integer = int(input("Enter number: "))
except Exception as e:
    print(f"Error: {e}")
    exit(0)

print(integer, end=" ")

while integer != 1:
    integer = collatz(integer)
