print("Enter mass: ", end="")
mass = float(input())

print(
    f"{round(mass * 9.8)}\nToo heavy"
    if mass * 9.8 >= 500
    else f"{mass * 9.8}\nToo light" if mass * 9.8 <= 100 else f"{mass*9.8}"
)
