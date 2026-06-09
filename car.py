# object = an object is an instance of a class
# class = a class is a blueprint, that will describe attributes and methods, that an distinct type of object can have


# attributes = What an object is/has
# methods = What an object can do
# self = self is referring to the objecr we are currently working on

# The class name should always be in Capital!!
class Car:

    wheels = 4  # clas variable (default value)

    def __init__(self, make, model, year, color):

        self.make = make   # instance variables
        self.model = model    # instance variables
        self.year = year    # instance variables
        self.color = color   # instance variables

# The variables which are declared inside the constructor are called as Instance Variables.

    def drive(self):
        print("This "+self.model+" is driving")
    def stop(self):
        print("This "+self.model+" is stopped")

