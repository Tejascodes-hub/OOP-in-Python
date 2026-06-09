# method chaining = it is used to call multiple methods sequentially.
#                   each call performs an action on the same object and returns self

# FOR USING METHOD-CHAINING, ENTER (RETURN SELF), IN EVERY METHOD, WE WANT TO USE METHOD CHAINING WITH.

class Car:

    def turn_on(self):
        print("You turned-on the car")
        return self

    def drive(self):
        print("You are driving the car")
        return self

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print("You turned-off the car")
        return self

# BY NORMAL METHOD:
car = Car()

#car.turn_on()
#car.drive()


# USING METHOD CHAINING: 

# both the code below has the same meaning.

# this code, will print everything, without much code.
car.turn_on().drive().brake().turn_off()

car.turn_on()\
.drive()\
.brake()\
.turn_off()