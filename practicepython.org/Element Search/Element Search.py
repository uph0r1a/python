import random


def binary_search(ls, n):
    low = 0
    high = len(ls) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = ls[middle]

        if guess == n:
            return True
        elif guess > n:
            high = middle - 1
        else:
            low = middle + 1
    return False


ls = sorted([random.randint(1, 100) for _ in range(random.randint(1, 20))])
print(ls)
if binary_search(ls, int(input("Enter a number: "))):
    print("Found")
else:
    print("Not found")
