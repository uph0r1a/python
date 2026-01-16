girl_names = []
boy_names = []

try:
    with open("files/GirlNames.txt") as file:
        for line in file:
            girl_names.append(line.strip())

    with open("files/BoyNames.txt") as file:
        for line in file:
            boy_names.append(line.strip())

except Exception as e:
    print(f"\nError: {e}")

boy = input("Enter a boy's name (or press Enter to skip): ").strip()
girl = input("Enter a girl's name (or press Enter to skip): ").strip()

if boy:
    if boy in boy_names:
        print(f"\n{boy} is one of the most popular boy names.")
    else:
        print(f"\n{boy} is NOT one of the most popular boy names.")

if girl:
    if girl in girl_names:
        print(f"\n{girl} is one of the most popular girl names.")
    else:
        print(f"\n{girl} is NOT one of the most popular girl names.")
