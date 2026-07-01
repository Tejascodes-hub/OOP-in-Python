# sort() method = used with lists
# sort() function = used with iterables
# this works alphabetically.

# sort() method :
#students = ["Tejas", "Samarth", "Bhavya", "Soham", "Shreyas", "Nihar"]
#students.sort()
#for i in students:
    #print(i)

#print("--------------------------------------------------------------------")
# sort() function :

#college_friends = ("samarth", "soham", "bhavya", "shreyash", "nihar")
#sorted_clg_friends = sorted(college_friends, reverse=True)
#for i in sorted_clg_friends:
   # print(i)

# dealing with lists of tuples:

family = [("Ramesh", "Dad", 60),
          ("Mangala", "Mom", 50),
          ("Avantka", "Sister", 25)]

# the index is been entered column wise.
age = lambda age:age[2]
#family.sort(key=age)

# same by sorted functions:
sorted_family = sorted(family, key=age)
for i in sorted_family:
    print(i)
