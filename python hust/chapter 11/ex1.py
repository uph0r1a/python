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


class ProductionWorker(Employee):
    def __init__(self, name="", number=0, shift=1, pay_rate=0):
        super().__init__(name, number)
        if 1 <= shift <= 2:
            self.__shift = shift
        self.__pay_rate = pay_rate

    def set_shift(self, shift=1):
        self.__shift = shift

    def set_pay_rate(self, pay_rate=0):
        if 1 <= pay_rate <= 2:
            self.__pay_rate = pay_rate

    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate


name = input("Enter worker name: ")
while 1:
    number = int(input("Enter worker number: "))
    if number > 0:
        break
    print("Worker number must be positive\n")
while 1:
    shift = int(input("Enter worker shift number: "))
    if 1 <= shift <= 2:
        break
    print("Worker shift must be 1 or 2\n")
while 1:
    pay_rate = int(input("Enter worker pay rate: "))
    if pay_rate >= 0:
        break
    print("Worker pay rate must be positive\n")

worker = ProductionWorker(name, number, shift, pay_rate)

print(
    f"Name: {worker.get_name()}\nNumber: {worker.get_number()}\nShift number: {"Day" if worker.get_shift() == 1  else  "Night"}\nPay rate: {worker.get_pay_rate()}"
)
