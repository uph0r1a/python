aList = list(map(int, input().split()))
aList.remove(min(aList))
print(min(aList))