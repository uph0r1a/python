print("Enter the number of packages purchased: ", end="")
numberOfPackage = int(input())

if numberOfPackage >= 100:
    print(
        f"Discount: 40%\nTotal amount of the purchase after the discount: {99 * numberOfPackage * 0.4}"
    )
elif 50 <= numberOfPackage <= 99:
    print(
        f"Discount: 30%\nTotal amount of the purchase after the discount: {99 * numberOfPackage * 0.3}"
    )
elif 20 <= numberOfPackage <= 49:
    print(
        f"Discount: 20%\nTotal amount of the purchase after the discount: {99 * numberOfPackage * 0.2}"
    )
elif 10 <= numberOfPackage <= 19:
    print(
        f"Discount: 10%\nTotal amount of the purchase after the discount: {99 * numberOfPackage * 0.1}"
    )
else:
    print("Invalid number of package")
