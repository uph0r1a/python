class Patient:
    def __init__(
        self,
        first_name="",
        middle_name="",
        last_name="",
        address="",
        city="",
        state="",
        ZIP_code="",
        phone_number="",
        emergency_contact_name="",
        emergency_contact_number="",
    ):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__ZIP_code = ZIP_code
        self.__phone_number = phone_number
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_number = emergency_contact_number

    def set_first_name(self, first_name=""):
        self.__first_name = first_name

    def set_middle_name(self, middle_name=""):
        self.__middle_name = middle_name

    def set_last_name(self, last_name=""):
        self.__last_name = last_name

    def set__address(self, address=""):
        self.__address = address

    def set_city(self, city=""):
        self.__city = city

    def set_state(self, state=""):
        self.__state = state

    def set_ZIP_code(self, ZIP_code=""):
        self.__ZIP_code = ZIP_code

    def set_phone_number(self, phone_number=""):
        self.__phone_number = phone_number

    def set_emergency_contact_name(self, emergency_contact_name=""):
        self.__emergency_contact_name = emergency_contact_name

    def set_emergency_contact_number(self, emergency_contact_number=""):
        self.__emergency_contact_number = emergency_contact_number

    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_ZIP_code(self):
        return self.__ZIP_code

    def get_phone_number(self):
        return self.__phone_number

    def get_emergency_contact_name(self):
        return self.__emergency_contact_name

    def get_emergency_contact_number(self):
        return self.__emergency_contact_number


class Procedure:
    def __init__(
        self,
        procedure_name="",
        procedure_date="",
        practitioner_name="",
        procedure_charges=0,
    ):
        self.__procedure_name = procedure_name
        self.__procedure_date = procedure_date
        self.__practitioner_name = practitioner_name
        self.__procedure_charges = procedure_charges

    def set_procedure_name(self, procedure_name=""):
        self.__procedure_name = procedure_name

    def set_procedure_date(self, procedure_date=""):
        self.__procedure_date = procedure_date

    def set_practitioner_name(self, practitioner_name=""):
        self.__practitioner_name = practitioner_name

    def set_procedure_charges(self, procedure_charges=0):
        self.__procedure_charges = procedure_charges

    def get_procedure_name(self):
        return self.__procedure_name

    def get_procedure_date(self):
        return self.__procedure_date

    def get_practitioner_name(self):
        return self.__practitioner_name

    def get_procedure_charges(self):
        return self.__procedure_charges


patient = Patient(
    "Emily",
    "Rose",
    "Johnson",
    "88 Maple Avenue",
    "Austin",
    "Texas",
    "78701",
    "+1 512-555-0178",
    "Robert Johnson",
    "+1 512-555-0142",
)
procedures = [
    Procedure("Physical Exam", "23/4/2026", "Dr. Irvine", 250.00),
    Procedure("X-ray", "23/4/2026", "Dr. Jamison", 500.00),
    Procedure("Blood test", "23/4/2026", "Dr. Smith", 200.00),
]

print(
    f"Name: {patient.get_first_name() + " " + patient.get_middle_name() + " " + patient.get_last_name()}\nAddress: {patient.get_address()}\nCity: {patient.get_city()}\nState: {patient.get_state()}\nZIP code: {patient.get_ZIP_code()}\nPhone number: {patient.get_phone_number()}\nEmergency contact name: {patient.get_emergency_contact_name()}\nEmergency contect phone number: {patient.get_emergency_contact_number()}\n"
)

for procedure in procedures:
    print(
        f"Procedure name: {procedure.get_procedure_name()}\nDate: {procedure.get_procedure_date()}\nPractitioner: {procedure.get_practitioner_name()}\nCharge: {procedure.get_procedure_charges()}\n"
    )
