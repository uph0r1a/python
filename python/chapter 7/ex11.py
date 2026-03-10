def isLoshu(square):
    if len(square) != 3:
        return False

    for row in square:
        if len(row) != 3:
            return False

    nums = []
    for row in square:
        for num in row:
            nums.append(num)

    nums.sort()
    if nums != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False

    for row in square:
        if sum(row) != 15:
            return False

    for col in range(3):
        col_sum = 0
        for row in range(3):
            col_sum += square[row][col]
        if col_sum != 15:
            return False

    if square[0][0] + square[1][1] + square[2][2] != 15:
        return False

    if square[0][2] + square[1][1] + square[2][0] != 15:
        return False

    return True


square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
print("Is a Lo Shu Square" if isLoshu(square) else "Is not a Lo Shu Square")
