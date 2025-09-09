dontCare = input()
S = input()
point = 0
index = S.find("luyencode")
while index != -1:
    S = S.replace("luyencode", "", 1)
    point += 1
    index = S.find("luyencode")
print(point)
