class Person:
    def __init__(self, name="", address="", tel=""):
        self.__name = name
        self.__address = address
        self.__tel = tel

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_tel(self):
        return self.__tel


class Customer(Person):
    def __init__(
        self, name="", address="", tel="", customer_number=0, mailing_list=False
    ):
        super().__init__(name, address, tel)
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def get_customer_number(self):
        return self.__customer_number

    def get_mailing_list(self):
        return self.__mailing_list


customer = Customer("Name", "Address", "Tel", "Number", True)

print(
    f"Name: {customer.get_name()}\nAddress: {customer.get_address()}\nTel number: {customer.get_tel()}\nCustomer number: {customer.get_customer_number()}\nMailing list: {"Yes" if customer.get_mailing_list() else "No"}"
)
