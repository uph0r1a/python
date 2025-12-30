with open("test.inp", "r") as f:
    numbers = list(map(int, f.read().split()))
flag = False
index = 0
while True:
    if index == len(numbers):
        if flag:
            index = 0
            flag = False
        else:
            break
    
    for i in numbers[index+1:]:
        if numbers[index] > i:
            position1 = index
            position2 = numbers.index(i)
            numbers[position1], numbers[position2] = numbers[position2], numbers[position1]
            flag = True
            break
    index += 1

with open("test.out", "w") as f:
    result = ""
    for i in numbers:
        result = result + str(i) + " "
    f.write(result)
