def display_greater_than(numbers, n):
    for value in numbers:
        if value > n:
            print(value)


nums = [3, 7, 1, 9, 4, 12, 6]
n = int(input("Enter a number: "))

display_greater_than(nums, n)
