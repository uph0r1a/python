print("Is anyone in your party a vegetarian: ", end="")
vegetarian = input()

print("Is anyone in your party a vegan: ", end="")
vegan = input()

print("Is anyone in your party a gluten-free: ", end="")
glutenFree = input()

print("Here are your restaurant choices:")

if vegetarian.lower() == "no" and vegan.lower() == "no" and glutenFree.lower() == "no":
    print("Joe's Gourmet Burgers")

if (
    vegetarian.lower() == "yes"
    and vegan.lower() == "no"
    and glutenFree.lower() == "yes"
):
    print("Main Street Pizza Company")

if (
    vegetarian.lower() == "yes"
    and vegan.lower() == "yes"
    and glutenFree.lower() == "yes"
):
    print("Corner Cafe")

if vegetarian.lower() == "yes" and vegan.lower() == "no" and glutenFree.lower() == "no":
    print("Mama's Fine Italian")

if (
    vegetarian.lower() == "yes"
    and vegan.lower() == "yes"
    and glutenFree.lower() == "yes"
):
    print("The Chef's Kitchen")
