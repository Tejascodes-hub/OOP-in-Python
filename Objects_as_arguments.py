class Car:

    color = None

class Motocycle:
    color = None

def change_color(car, color):
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Motocycle()

change_color(car_1, "Red")
change_color(car_2, "blue")
change_color(car_3, "black")
change_color(bike_1, "purple")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)