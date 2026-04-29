def main():
    numbers = []
    powerballs = []

    with open("files/pbnumbers.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            values = line.split()
            nums = values[:5]
            pb = values[5]

            numbers.extend(nums)
            powerballs.append(pb)

    num_freq = {}
    pb_freq = {}

    for n in numbers:
        num_freq[n] = num_freq.get(n, 0) + 1

    for p in powerballs:
        pb_freq[p] = pb_freq.get(p, 0) + 1

    print("10 Most Common Numbers:")
    for num, count in sorted(num_freq.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(num, count)

    print("\n10 Least Common Numbers:")
    for num, count in sorted(num_freq.items(), key=lambda x: x[1])[:10]:
        print(num, count)

    last_seen = {}
    total_draws = len(lines)

    for index, line in enumerate(lines):
        values = line.split()
        for num in values[:5]:
            last_seen[num] = index

    overdue = sorted(last_seen.items(), key=lambda x: total_draws - x[1], reverse=True)[
        :10
    ]

    print("\n10 Most Overdue Numbers:")
    for num, index in overdue:
        print(num)

    print("\nFrequency of numbers 1-69:")
    for i in range(1, 70):
        print(i, num_freq.get(str(i).zfill(2), 0))

    print("\nFrequency of PowerBall numbers 1-26:")
    for i in range(1, 27):
        print(i, pb_freq.get(str(i).zfill(2), 0))


if __name__ == "__main__":
    main()
