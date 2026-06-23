# Lambda function = function written in one line using lambda keyword
# accepts any number of arguments, but only has one expression.
# (think of it as a shortcut)
# (useful if needed for a short period of time, throw-away).

# SYNTAx --> lambda parameters:expression
# normal way to write
def double(x):
    return x * 2
print(double(5))


# by using (lambda function) :
double = lambda x : x * 2
print(double(5))

# using two parameters :
multiply = lambda x, y : x * y
print(multiply(4,4))

# adding 3 numbers together :
add = lambda x, y, z : x + y + z 
print(add(5,3,5))

# complex :
full_name = lambda first_name, last_name : first_name + last_name
print(full_name("Tejas ", "chapegadikar"))
age_check = lambda age : True if age >= 18 else False
print(age_check(18))



