# Multi-level inheritance = When a derived (child) class inherits another (child) class.

# Lets create a (FAMILY TREE OF LIVING ORGANISMS).
class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")
    
class Dog(Animal):

    def bark(self):
        print("The dog is barking")

# here (dog class) is child --> (Animal class) is parent --> (Organism class) is grandparent

Dog = Dog()

print(Dog.alive)
Dog.eat()
Dog.bark()
