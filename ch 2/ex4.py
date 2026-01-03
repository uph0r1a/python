subTotal = saleTax = total = 0
for i in range(5):
    print(f"Enter item {i+1} price: ", end="")
    price = float(input())
    subTotal += price
    saleTax += price * 0.07

total += subTotal + saleTax

print(f"Sub total: {subTotal}\nSale tax: {round(saleTax,2)}\nTotal: {total}")
