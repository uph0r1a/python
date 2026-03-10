print(f"{"Celsius":<10}{"Fahrenheit":<10}\n--------------------")
for i in range(21):
    print(f"{i:<10}{round((9 / 5) * i + 32,2):<10}")
