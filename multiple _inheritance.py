# multiple inheritance is a concept when a child class is derived from more than one parent class.

class prey:

    def flee(self):
        print("This animal flee's")

class predator:

    def hunt(self):
        print("This animal hunt's")
    

class Rabbit(prey):
    pass
class Hawk(predator):
    pass
class Fish(prey, predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

fish.flee()
fish.hunt()
