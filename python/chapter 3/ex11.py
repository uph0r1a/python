print("Enter the number of books purchased this month: ", end="")
numberOfBook = int(input())

if numberOfBook == 0:
    print("0 point")
elif numberOfBook == 2:
    print("5 points")
elif numberOfBook == 4:
    print("15 points")
elif numberOfBook == 6:
    print("30 points")
elif numberOfBook >= 8:
    print("60 points")
else:
    print("Invalid number of book")
