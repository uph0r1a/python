hour = int(input())
minute = int(input())
second = int(input())
second += 5
if second >= 60:
    PlusMinutes = second // 60
    second = second % 60
    minute += PlusMinutes

if minute >= 60:
    PlusHours = minute // 60
    minute = minute % 60
    hour += PlusHours

print(f"{hour:02d}:{minute:02d}:{second:02d}")