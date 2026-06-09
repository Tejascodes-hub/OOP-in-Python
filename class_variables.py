from car import Car

car_1 = Car("Lamborgini", "Aventador", 2015, "Green")
car_2 = Car("Ferrari", "SF90", 2017, "Red")

print("Default value of class variable:")
print(car_1.wheels)
print(car_2.wheels)

print("---------------------------------------------------------------")

print("Changed value of class variable:")
# we can also change the class variable here, imagine car_1 has 2 wheels:
car_1.wheels = 2
print(car_1.wheels)

# we can also change the class variable here, imagine car_2 has 6 wheels:

car_2.wheels = 6
print(car_2.wheels  )