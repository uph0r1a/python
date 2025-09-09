def main():
    second: int = int(input())
    result: str = timeConverter(second)
    print(result)


def timeConverter(second: int) -> str:
    hour = second // (60 * 60)
    leftover = second % (60 * 60)
    minute = leftover // 60
    second = leftover % 60
    return f"{hour:02d}:{minute:02d}:{second:02d}"


main()
