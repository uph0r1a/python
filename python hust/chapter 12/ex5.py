def sum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sum(lst[1:])


l = [1, 2, 3, 4, 5]
print(sum(l))
