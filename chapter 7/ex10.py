winners = []

try:
    with open("files/WorldSeriesWinners.txt") as file:
        for line in file:
            winners.append(line.strip())

except Exception as e:
    print(f"\nError: {e}")

team = input("Enter the name of a team: ").strip()

count = 0
for winner in winners:
    if winner == team:
        count += 1

print(f"\n{team} won the World Series {count} times from 1903 through 2009.")
