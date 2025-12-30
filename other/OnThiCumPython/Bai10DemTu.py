with open("test.inp", "r") as f:
    phung = f.read()

howManyTu = len(list(phung.split()))
eilam = set()
for char in phung:
    if char.isalpha():
        eilam.add(char)

with open("test.out", "w") as f:
    f.writelines(f"{howManyTu}\n{len(eilam)}")



