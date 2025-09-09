def maxNum(numbers: list[int] | tuple[int] | set[int]) -> int:
    return max(*numbers)


lolHi = tuple(map(int, input().split()))
print(maxNum(lolHi))
