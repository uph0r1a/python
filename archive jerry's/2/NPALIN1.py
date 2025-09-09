def main():
    howMany = int(input("Bao nhiêu test? >"))
    tests = []
    for _ in range(howMany):
        tests.append(int(input()))

    results = []
    for i in tests:
        results.append(testing(i))

    for result in results:
        print(result)


def testing(n: int) -> int:
    limit = int("1" + "0" * n)
    start = int("1" + "0" * (n - 1))
    result = 0
    for number in range(start, limit):
        reversedNumber = 0
        dummy = number
        while dummy > 0:
            remainder = dummy % 10
            reversedNumber = (reversedNumber * 10) + remainder
            dummy = dummy // 10
        if number == reversedNumber:
            result += 1
    return result


main()
