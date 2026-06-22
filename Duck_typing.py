# Duck typing = concept when the class of an object is less important than the methods/attributes.
# class type is not checked if minimum methods/attributes are present
# "if it walks like a duck, and it quacks like a duck, then it must be a duck."

# self = self is passed so a method can access and modify the attributes and methods of the specific object that called it.

# simple explanation --> If an object has the required method/behavior, Python uses it without caring what class the object belongs to.

class Duck:
    
    def walk(self):
        print("the duck is walking")
    def run(self):
        print("the duck is running")
    
class Dog:
    
    def walk(self):
        print("the dog is walking")
    def run(self):
        print("the dog is running")

class Person:
    def catch(self, duck):
        duck.walk()
        duck.run()

        print("it ran away!")

duck = Duck()
dog = Dog()
person = Person()

person.catch(dog)