class Employee:
    def __init__(self, name="", id=0, department="", title=""):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title


employee = [
    Employee("Susan Meyers", 47899, "Accounting", "Vice President"),
    Employee("Mark Jones", 39119, "IT", "Programmer"),
    Employee("Joy Rogers", 81774, "Manufacturing", "Engineer"),
]

for empl in employee:
    print(
        f"Name: {empl.get_name()}\nID Number: {empl.get_id()}\nDepartment: {empl.get_department()}\nJob Title: {empl.get_title()}\n"
    )
