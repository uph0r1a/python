try:
    with open("text1.txt") as f1, open("text2.txt") as f2:
        set1 = {int(line.strip()) for line in f1}
        set2 = {int(line.strip()) for line in f2}
except Exception as e:
    print(f"Error: {e}")

print(list(set1 & set2))
