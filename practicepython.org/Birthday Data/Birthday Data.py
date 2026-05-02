import json, os
from bokeh.plotting import figure, show
from bokeh.io import output_file

while True:
    os.system("clear")

    try:
        choice = int(
            input(
                "1) Add new birthday\n"
                "2) Search for birthday\n"
                "3) Month List\n"
                "4) Birthday Plots\n"
                "Enter your choice: "
            )
        )
    except ValueError:
        print("Invalid input. Please enter a number.")
        input("Press Enter to continue...")
        continue

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice")
        input("Press Enter to continue...")
        continue

    os.system("clear")

    file_path = "birthday.json"

    if choice == 1:
        name_input = input("Enter name: ")
        birthday_input = input("Enter birthday: ")

        try:
            try:
                with open(file_path, "r") as f:
                    birthday = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                birthday = {}

            birthday[name_input] = birthday_input

            with open(file_path, "w") as f:
                json.dump(birthday, f, indent=4)

        except Exception as e:
            print(f"Error: {e}")

    elif choice == 2:
        name_input = input("Enter name: ")

        try:
            with open(file_path, "r") as f:
                birthday = json.load(f)

            print(birthday.get(name_input, "Name not found"))

        except Exception as e:
            print(f"Error: {e}")

    elif choice == 3:
        try:
            month = {
                "january": 0,
                "february": 0,
                "march": 0,
                "april": 0,
                "may": 0,
                "june": 0,
                "july": 0,
                "august": 0,
                "september": 0,
                "october": 0,
                "november": 0,
                "december": 0,
            }

            with open(file_path, "r") as f:
                birthday = json.load(f)

            for value in birthday.values():
                value = value.lower()

                for key in month:
                    if key in value:
                        month[key] += 1

            print(month)

        except Exception as e:
            print(f"Error: {e}")

    elif choice == 4:
        try:
            month = {
                "january": 0,
                "february": 0,
                "march": 0,
                "april": 0,
                "may": 0,
                "june": 0,
                "july": 0,
                "august": 0,
                "september": 0,
                "october": 0,
                "november": 0,
                "december": 0,
            }

            with open(file_path, "r") as f:
                birthday = json.load(f)

            for value in birthday.values():
                value = value.lower()
                for key in month:
                    if key in value:
                        month[key] += 1

            months = list(month.keys())
            counts = list(month.values())

            output_file("birthday_histogram.html")

            p = figure(
                x_range=months,
                title="Birthday Count by Month",
                x_axis_label="Month",
                y_axis_label="Number of Birthdays",
                height=400,
                width=800,
            )

            p.vbar(x=months, top=counts, width=0.8)

            p.xaxis.major_label_orientation = 1.0

            show(p)

        except Exception as e:
            print(f"Error: {e}")

    while True:
        cont = input("Do you want to continue (Y/N)? ").strip().upper()
        if cont in ["Y", "N"]:
            break
        print("Invalid choice")

    if cont == "N":
        break
