import pickle

FILE_NAME = "files/emails.dat"


def load_data():
    try:
        with open(FILE_NAME, "rb") as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Error: {e}")
        return {}


def save_data(emails):
    with open(FILE_NAME, "wb") as file:
        pickle.dump(emails, file)


def main():
    emails = load_data()

    while True:
        print("\nMenu")
        print("1. Look up an email address")
        print("2. Add a new name and email address")
        print("3. Change an existing email address")
        print("4. Delete a name and email address")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            if name in emails:
                print("Email:", emails[name])
            else:
                print("Name not found.")

        elif choice == "2":
            name = input("Enter name: ")
            email = input("Enter email: ")
            emails[name] = email
            print("Entry added.")

        elif choice == "3":
            name = input("Enter name: ")
            if name in emails:
                emails[name] = input("Enter new email: ")
                print("Email updated.")
            else:
                print("Name not found.")

        elif choice == "4":
            name = input("Enter name: ")
            if name in emails:
                del emails[name]
                print("Entry deleted.")
            else:
                print("Name not found.")

        elif choice == "5":
            save_data(emails)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
