from car import Car

# In python, we donot need to pass anything in (Self)
# we can use the same class as a blueprint, to create more car objects.
car_1 = Car("Lamborgini", "Aventador", 2015, "Green")
car_2 = Car("Ferrari", "SF90", 2017, "Red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

print("---------------------------------------------------------------")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()