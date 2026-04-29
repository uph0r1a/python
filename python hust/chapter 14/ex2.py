import sqlite3

DB_NAME = "files/phonebook.db"


def connect():
    conn = sqlite3.connect(DB_NAME)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS Entries (
                        EntryID     INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name        TEXT    NOT NULL,
                        PhoneNumber TEXT    NOT NULL)"""
    )
    conn.commit()
    return conn


def add_entry(conn, name, phone):
    conn.execute("INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)", (name, phone))
    conn.commit()
    print(f"\n  ✔  '{name}' added to the phonebook.")


def lookup_entry(conn, name):
    cur = conn.execute(
        "SELECT Name, PhoneNumber FROM Entries WHERE Name LIKE ?", (f"%{name}%",)
    )
    rows = cur.fetchall()
    if rows:
        print(f"\n  {'Name':<25} {'Phone Number'}")
        print("  " + "-" * 42)
        for r in rows:
            print(f"  {r[0]:<25} {r[1]}")
    else:
        print(f"\n  No entries found matching '{name}'.")


def update_entry(conn, name, new_phone):
    cur = conn.execute(
        "UPDATE Entries SET PhoneNumber = ? WHERE Name LIKE ?", (new_phone, f"%{name}%")
    )
    conn.commit()
    if cur.rowcount:
        print(f"\n  ✔  Updated {cur.rowcount} entry/entries matching '{name}'.")
    else:
        print(f"\n  No entries found matching '{name}'.")


def delete_entry(conn, name):
    cur = conn.execute(
        "SELECT EntryID, Name, PhoneNumber FROM Entries WHERE Name LIKE ?",
        (f"%{name}%",),
    )
    rows = cur.fetchall()
    if not rows:
        print(f"\n  No entries found matching '{name}'.")
        return
    print(f"\n  Matching entries:")
    print(f"  {'ID':<5} {'Name':<25} {'Phone Number'}")
    print("  " + "-" * 45)
    for r in rows:
        print(f"  {r[0]:<5} {r[1]:<25} {r[2]}")
    confirm = input("\n  Delete these entries? (y/n): ").strip().lower()
    if confirm == "y":
        conn.execute("DELETE FROM Entries WHERE Name LIKE ?", (f"%{name}%",))
        conn.commit()
        print(f"  ✔  Deleted {len(rows)} entry/entries.")
    else:
        print("  Deletion cancelled.")


def display_all(conn):
    cur = conn.execute("SELECT EntryID, Name, PhoneNumber FROM Entries ORDER BY Name")
    rows = cur.fetchall()
    if rows:
        print(f"\n  {'ID':<5} {'Name':<25} {'Phone Number'}")
        print("  " + "-" * 45)
        for r in rows:
            print(f"  {r[0]:<5} {r[1]:<25} {r[2]}")
        print(f"\n  Total entries: {len(rows)}")
    else:
        print("\n  The phonebook is empty.")


MENU = """
╔══════════════════════════════════╗
║       Phonebook Application      ║
╠══════════════════════════════════╣
║  1. Add an entry                 ║
║  2. Look up a phone number       ║
║  3. Change a phone number        ║
║  4. Delete an entry              ║
║  5. Display all entries          ║
║  0. Exit                         ║
╚══════════════════════════════════╝
Choice: """


def main():
    conn = connect()
    print(f"\n  Connected to '{DB_NAME}'.")

    while True:
        choice = input(MENU).strip()

        if choice == "1":
            name = input("\n  Enter name:         ").strip()
            phone = input("  Enter phone number: ").strip()
            if name and phone:
                add_entry(conn, name, phone)
            else:
                print("  Name and phone number cannot be empty.")

        elif choice == "2":
            name = input("\n  Enter name to look up: ").strip()
            lookup_entry(conn, name)

        elif choice == "3":
            name = input("\n  Enter name to update:    ").strip()
            phone = input("  Enter new phone number:  ").strip()
            if phone:
                update_entry(conn, name, phone)
            else:
                print("  Phone number cannot be empty.")

        elif choice == "4":
            name = input("\n  Enter name to delete: ").strip()
            delete_entry(conn, name)

        elif choice == "5":
            display_all(conn)

        elif choice == "0":
            print("\n  Goodbye!\n")
            break

        else:
            print("\n  Invalid choice. Please enter 0-5.")

    conn.close()


if __name__ == "__main__":
    main()
