import math

print("Enter the speed of a vehicle (in miles per hour): ", end="")
speed = float(input())

print("Enter the number of hours it has traveled: ", end="")
time = float(input())

print(f"{"Hour":<10}{"Distance Traveled":<20}\n---------------------------")

for i in range(1, math.floor(time) + 1):
    print(f"{i:<10}{speed * i:<20}")
