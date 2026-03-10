def main():
    team_wins = {}
    year_winner = {}

    start_year = 1903

    try:
        with open("files/WorldSeriesWinners.txt") as file:
            for i, line in enumerate(file):
                year = start_year + i
                winner = line.strip()

                if winner == "World Series Not Played":
                    continue

                year_winner[year] = winner
                team_wins[winner] = team_wins.get(winner, 0) + 1

    except Exception as e:
        print(f"Error: {e}")
        return

    year = int(input("Enter a year between 1903 and 2009: "))

    if year in year_winner:
        team = year_winner[year]
        print(f"Winner in {year}: {team}")
        print(f"Total World Series wins: {team_wins[team]}")
    else:
        print("The World Series was not played that year.")


main()
