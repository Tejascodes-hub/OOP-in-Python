# Prevents a user from creating an object of thst class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

# simple explanation --> our Vehivle class is telling its children, if you are going to inherit from me then, you need to override this abstarct method of mine, if you dont we are not going to let you instantiate it.


# Now, Car and Bike --> both must implement the abstract methods, which are (go) & (stop).
# and call the methods accordingly.
from abc import ABC, abstractmethod

class Vehicle:

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You are driving the Car")

    def stop(self):
        print("This car is stopped")

class Bike(Vehicle):

    def go(self):
        print("You are riding a bike")

    def stop(self):
        print("This Bike is stopped")

vehicle = Vehicle()
car = Car()
bike = Bike()

car.go()
car.stop()
bike.go()
bike.stop()
  
