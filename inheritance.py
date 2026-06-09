# inheritance --> In this parent class inherit it's properties to the child.
# in the code below --> Animal is a parent class and rabbit is a child class.

class Animal:

    alive = True

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")

class Rabbit(Animal):
    
    def run(self):
        print("The Rabbit is running")

class Dog(Animal):
    
    def bark(slef):
        print("The dog is barking")

class Cat(Animal):
    
    def black(self):
        print("That Cat is black in color")

Rabbit = Rabbit()
Dog = Dog()
Cat = Cat()

#print(Rabbit.alive)
#Dog.eat()
#Cat.sleep()

Rabbit.run()
Dog.bark()
Cat.black()

# conclusion --> Classes can have children, children classes inherit everything that its parent class has

# The children classes can also implement its own unique attributes and methods aswell!!