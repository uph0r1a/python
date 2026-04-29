class Car:
    def __init__(self, year_model=0, make=""):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed < 5:
            self.__speed = 0
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


car = Car(2020, "Ford")

print(f"Speed: {car.get_speed()}")

car.accelerate()
car.accelerate()
car.accelerate()
car.accelerate()
car.accelerate()

print(f"Speed: {car.get_speed()}")

car.brake()
car.brake()
car.brake()
car.brake()
car.brake()

print(f"Speed: {car.get_speed()}")
