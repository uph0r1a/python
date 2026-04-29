import random

a = [random.randint(1, 100) for _ in range(random.randint(1, 20))]
b = [random.randint(1, 100) for _ in range(random.randint(1, 20))]

print("List 1: " + str(a))
print("List 2: " + str(b))

print("Overlap: " + str(set([i for i in a if i in b])))
