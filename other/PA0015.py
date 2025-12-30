# Bài 6
total = 4
rice = 0
currentbox = 1
for i in range(1, total+1):
    rice += currentbox
    currentbox *= 2
print(rice)