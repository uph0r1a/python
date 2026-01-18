def main():
    team_wins = {}
    year_winner = {}

    start_year = 1903
    year = start_year

    with open("files/WorldSeriesWinners.txt") as file:
        for line in file:
            winner = line.strip()

            if winner == "World Series Not Played":
                year += 1
                continue

            year_winner[year] = winner

            if winner in team_wins:
                team_wins[winner] += 1
            else:
                team_wins[winner] = 1

            year += 1

    user_year = int(input("Enter a year between 1903 and 2009: "))

    if user_year in year_winner:
        team = year_winner[user_year]
        print(f"Winner in {user_year}: {team}")
        print(f"Total World Series wins: {team_wins[team]}")
    else:
        print("The World Series was not played that year.")


if __name__ == "__main__":
    main()
