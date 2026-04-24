import sys, pickle, os


class Employee:
    def __init__(self, name="", id=0, department="", title=""):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title

    def set_name(self, name):
        self.__name = name

    def set_department(self, department):
        self.__department = department

    def set_title(self, title):
        self.__title = title

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title


employee = {
    47899: Employee("Susan Meyers", 47899, "Accounting", "Vice President"),
    39119: Employee("Mark Jones", 39119, "IT", "Programmer"),
    81774: Employee("Joy Rogers", 81774, "Manufacturing", "Engineer"),
}


while 1:
    os.system("clear")
    print(
        "1)Look up an employee in the dictionary\n2)Add a new employee to the dictionary\n3)Change an existing employee's name, department, and job title in the dictionary\n4)Delete an employee from the dictionary\n5)Quit the program\nEnter your choice: ",
        end="",
    )

    match int(input()):
        case 1:
            os.system("clear")
            find = int(input("Enter employee ID: "))
            if find in employee:
                print(
                    f"Name: {employee[find].get_name()}\nID Number: {employee[find].get_id()}\nDepartment: {employee[find].get_department()}\nJob Title: {employee[find].get_title()}\n"
                )
            else:
                print("Employee not exist")

        case 2:
            os.system("clear")
            name = input("Enter name: ")
            while 1:
                id = int(input("Enter ID number: "))
                if id not in employee:
                    break
                else:
                    print("ID exist\n")
            department = input("Enter department: ")
            title = input("Enter job title: ")

            employee[id] = Employee(name, id, department, title)

        case 3:
            os.system("clear")
            while 1:
                id = int(input("Enter ID number: "))
                if id in employee:
                    break
                else:
                    print("ID dont exist\n")

            while 1:
                os.system("clear")
                choice = int(
                    input(
                        "1)Change name\n2)Change department\n3)Change title\nEnter your choice: "
                    )
                )
                match choice:
                    case 1:
                        employee[id].set_name(input("Enter new name: "))
                    case 2:
                        employee[id].set_department(input("Enter new department: "))
                    case 3:
                        employee[id].set_title(input("Enter new title: "))
                    case _:
                        print("Invalid choice\n")
                if input("Do you still want to change: ").lower() != "y":
                    break

        case 4:
            os.system("clear")
            while 1:
                id = int(input("Enter ID number: "))
                if id in employee:
                    break
                else:
                    print("ID dont exist\n")
            del employee[id]

        case 5:
            os.system("clear")
            try:
                with open("files/employee.pickle", "wb") as f:
                    pickle.dump(employee, f)
                print("Saved sucessfully\n")
            except Exception as e:
                print(f"Error: {e}")
            sys.exit()
