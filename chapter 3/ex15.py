import math

print("Enter a number of second: ", end="")
second = float(input())

day = hour = minute = 0

if second >= 86400:
    day = math.floor(second / 86400)
    second -= day * 86400

if second >= 3600:
    hour = math.floor(second / 3600)
    second -= hour * 3600

if second >= 60:
    minute = math.floor(second / 60)
    second -= minute * 60

print(f"{day} days, {hour} hours, {minute} minutes, {second} seconds")
