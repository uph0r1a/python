print("Enter the weight of a package: ", end="")
weight = float(input())

if weight >= 10:
    print(f"Shipping charge: ${weight * 4.75}")
elif 6 <= weight < 10:
    print(f"Shipping charge: ${weight * 4}")
elif 2 <= weight < 6:
    print(f"Shipping charge: ${weight * 3}")
elif 0 <= weight < 2:
    print(f"Shipping charge: ${weight * 1.5}")
else:
    print("Invalid weight")
