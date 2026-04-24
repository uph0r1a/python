class Employee:
    def __init__(self, name="", number=0):
        self.__name = name
        self.__number = number

    def set_name(self, name=""):
        self.__name = name

    def set_number(self, number=0):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


class ShiftSupervisor(Employee):
    def __init__(self, name="", number=0, annual_salary=0, annual_bonus=0):
        super().__init__(name, number)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_bonus(self):
        return self.__annual_bonus


name = input("Enter supervisor name: ")
while 1:
    number = int(input("Enter supervisor number: "))
    if number > 0:
        break
    print("Supervisor number must be positive\n")
while 1:
    annual_salary = int(input("Enter supervisor annual salary: "))
    if annual_salary >= 0:
        break
    print("Supervisor annual salary must be positive\n")
while 1:
    annual_bonus = int(input("Enter worker annual bonus: "))
    if annual_bonus >= 0:
        break
    print("Supervisor annual bonus must be positive\n")

supervisor = ShiftSupervisor(name, number, annual_salary, annual_bonus)

print(
    f"Name: {supervisor.get_name()}\nNumber: {supervisor.get_number()}\nAnnual salary: {supervisor.get_annual_salary()}\nAnnual bonus: {supervisor.get_annual_bonus()}"
)
