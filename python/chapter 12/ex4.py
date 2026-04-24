def largest_item(lst):
    if len(lst) == 1:
        return lst[0]

    max = largest_item(lst[1:])
    return lst[0] if lst[0] > max else max


l = [1, 10, 0, 9, 5]
print(largest_item(l))
