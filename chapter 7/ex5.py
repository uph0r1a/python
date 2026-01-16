accounts = []

try:
    with open("files/charge_accounts.txt") as file:
        for line in file:
            accounts.append(line.strip())

except Exception as e:
    print(f"\nError: {e}")

user_account = input("Enter a charge account number: ")

if user_account in accounts:
    print("\nThe charge account number is valid.")
else:
    print("\nThe charge account number is invalid.")
