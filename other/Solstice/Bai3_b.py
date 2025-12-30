nums = list(map(int, input().split()))
nums.remove(min(nums))
print(min(nums))