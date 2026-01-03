import math

print("Enter the number of people: ", end="")
numberOfPeople = int(input())

print("Enter the number of hotdog each people given: ", end="")
hotdogPerPeople = int(input())

print(
    f"The minimum number of packages of hot dogs required: {math.ceil(numberOfPeople*hotdogPerPeople / 10)}\nThe minimum number of packages of hot dog buns required: {math.ceil(numberOfPeople*hotdogPerPeople / 8)}\nThe number of hot dogs that will be left over: {(math.ceil(numberOfPeople*hotdogPerPeople / 10))*10 - (numberOfPeople*hotdogPerPeople)}\nThe number of hot dog buns that will be left over: {(math.ceil(numberOfPeople*hotdogPerPeople / 8))*8 - (numberOfPeople*hotdogPerPeople)}"
)
