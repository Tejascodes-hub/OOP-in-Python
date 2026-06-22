# walrus operator :=
# it assigns value to variable as part of a larger expression

# small eg : 
print(happy := True)


foods = list()
while True:
    food = input("what food do you like? : ")
    if food == "quit":
        break
    foods.append(food)

# same type of code, but in shortter way, by using (Walrus Operator).
 
drinks = list()
while drink := input("what is your favrite drink? : ") != "quit":
    drinks.append(drink)