list_a = [1, 8, 9, 15]
list_a.insert(1, 2)
list_a.append(4)

y = [
    [3, 5, 3],
    [2, 2, 5],
    [3, 8, 9],
]

for i in range(len(y)):
    for j in range(len(y[0])):
        print(y[j][i], end="\t")
    print("\n")
