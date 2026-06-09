# method overriding = When a child class provides its own version of a method that already exists in the parent class.

class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    def eat(self):
        print("The rabbit is eating a carrot!")

rabbit = Rabbit()
rabbit.eat()