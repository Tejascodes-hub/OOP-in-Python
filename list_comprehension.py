# List comprehention : a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read

# FORMULAS/SYNTAX:-
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression (if/else)for item in iterable]

#square = []               # create an empty list
#for i in range(1,11):     # create a for loop
 #   square.append(i * i)  # define what each loop iteration should do
#print(square)

# Now using list comprehension method

square = [i * i for i in range(1, 11)]
print(square)

students = [100, 30, 50, 70, 80, 90, 20, 10]
#passed_students = list(filter(lambda x : x >= 60, students))
# writing the same code by using (list comprehension)3

# only passed students:
passed_students = [i for i in students if i >= 60]

# passed + failed students:
list_students = [i if i >= 60 else "FAILED" for i in students]

print(list_students)
print(passed_students)