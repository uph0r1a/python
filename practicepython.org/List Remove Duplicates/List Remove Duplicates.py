def removeDupLoopList(n):
    result = []
    for i in n:
        if i not in result:
            result.append(i)

    return result


def removeDupSet(n):
    return list(set(n))


ls = [1, 1, 2, 3, 4, 5]

print("Original list: " + str(ls))
print("Using loop list: " + str(removeDupLoopList(ls)))
print("Using set: " + str(removeDupSet(ls)))
