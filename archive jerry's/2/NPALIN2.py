def main():
    howMany = int(input("Bao nhiêu test? >"))
    tests = []
    for _ in range(howMany):
        test = tuple(map(int, input().split()))
        tests.append(test)
    results = []
    for i in tests:
        results.append(testing(i))

    for result in results:
        print(result)


def testing(n: tuple[int]) -> int:
    start = n[0]
    limit = n[1]
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
