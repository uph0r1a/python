def falling_distance(t):
    return 0.5 * 9.8 * (t**2)


print("Enter the amount of time: ", end="")
time = float(input())

print(f"Distance: {falling_distance(time)}")
