# Higher order functions = a function that either : 1) accepts a function as an argument or 2) returns a function (In python, functions are also treated as objects)


# 1)
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Helloo")
    print(text)

hello(quiet)
hello(loud)

# 2)
def divisor(x):
    def divident(y):
        return y / x
    return divident

divide = divisor(2)
print(int(divide(10)))
# here, x = 2 and y = 10.

# here, divisor is a (higher order function), bcoz it returns a functions (divident)