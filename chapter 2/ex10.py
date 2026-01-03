print("Enter the amount of cookies: ", end="")
amount = int(input())

print(
    f"Cups of sugar needed: {(1.5/48)*amount}\nCups of butter needed: {(1/48)*amount}\nCups of flour needed: {(2.75/48)*amount}\n"
)
