# object = an object is an instance of a class
# class = a class is a blueprint, that will describe attributes and methods, that an distinct type of object can have


# attributes = What an object is/has
# methods = What an object can do
# self = self is referring to the objecr we are currently working on

# The class name should always be in Capital!!
class Car:

    
    def __init__(self, make, model, year, color):

        self.make = make
        self.model = model
        self.year = year
        self.color = color


    def drive(self):
        print("This "+self.model+" is driving")
    def stop(self):
        print("This "+self.model+" is stopped")

