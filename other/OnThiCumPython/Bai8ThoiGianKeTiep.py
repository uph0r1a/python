with open("test.inp", "r") as f:
    hour, minute, second = map(int, f.readlines())

second += 5
if second >= 60:
    minute += 1
    second = second % 60


if minute >= 60:
    hour += 1
    minute = minute % 60

with open("test.out", "w") as f:
    f.write(f"{hour:02d}:{minute:02d}:{second:02d}")