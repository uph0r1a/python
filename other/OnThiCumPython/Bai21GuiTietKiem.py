with open("test.inp", "r") as f:
    currentValue = float(f.read())

with open("test.out", "w") as f:
    f.write(f"nam thu 0 co {str(currentValue)} dong")
    for i in range(1, 11):
        currentValue += (currentValue * 7) / 100
        f.write(f"\nnam thu {i} co {str(currentValue)} dong")
