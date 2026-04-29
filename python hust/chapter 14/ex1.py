import sqlite3

MENU = """
========================================
        Cities Database Menu
========================================
 1. List cities by population (ascending)
 2. List cities by population (descending)
 3. List cities by name
 4. Total population of all cities
 5. Average population of all cities
 6. City with the highest population
 7. City with the lowest population
 0. Exit
========================================
Enter your choice: """


def print_cities(rows):
    print(f"\n{'#':<4}{'City':<22}{'Population':>15}")
    print("-" * 42)
    for i, (name, pop) in enumerate(rows, 1):
        print(f"{i:<4}{name:<22}{pop:>15,.0f}")


def main():
    conn = sqlite3.connect("files/cities.db")
    cur = conn.cursor()

    while True:
        choice = input(MENU).strip()

        if choice == "1":
            cur.execute(
                "SELECT CityName, Population FROM Cities ORDER BY Population ASC"
            )
            print("\nCities sorted by population (ascending):")
            print_cities(cur.fetchall())

        elif choice == "2":
            cur.execute(
                "SELECT CityName, Population FROM Cities ORDER BY Population DESC"
            )
            print("\nCities sorted by population (descending):")
            print_cities(cur.fetchall())

        elif choice == "3":
            cur.execute("SELECT CityName, Population FROM Cities ORDER BY CityName ASC")
            print("\nCities sorted by name:")
            print_cities(cur.fetchall())

        elif choice == "4":
            cur.execute("SELECT SUM(Population) FROM Cities")
            total = cur.fetchone()[0]
            print(f"\nTotal population of all cities: {total:,.0f}")

        elif choice == "5":
            cur.execute("SELECT AVG(Population) FROM Cities")
            avg = cur.fetchone()[0]
            print(f"\nAverage population of all cities: {avg:,.0f}")

        elif choice == "6":
            cur.execute(
                "SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1"
            )
            name, pop = cur.fetchone()
            print(f"\nCity with the highest population: {name} ({pop:,.0f})")

        elif choice == "7":
            cur.execute(
                "SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1"
            )
            name, pop = cur.fetchone()
            print(f"\nCity with the lowest population: {name} ({pop:,.0f})")

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please enter 0-7.")

    conn.close()


if __name__ == "__main__":
    main()
