import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [random.randint(1, 100) for _ in range(random.randint(1, 20))]
d = [random.randint(1, 100) for _ in range(random.randint(1, 20))]

overlap = list(dict.fromkeys(n for n in a if n in b))
overlapRand = list(dict.fromkeys(n for n in c if n in d))

print("List 1: " + str(a))
print("List 2: " + str(b))

print("Random list 1: " + str(c))
print("Random list 2: " + str(d))

print("Overlap list: " + str(overlap))
print("Overlap random list: " + str(overlapRand))
