# sort() method = used with lists
# sort() function = used with iterables
# this works alphabetically.

# sort() method :
students = ["Tejas", "Samarth", "Bhavya", "Soham", "Shreyas", "Nihar"]
students.sort()
for i in students:
    print(i)

print("--------------------------------------------------------------------")
# sort() function :

friends = ("ksj", "Sunny", "Roshan", "Priyanshu")
sorted_friends = sorted(friends)
for i in sorted_friends:
    print(i)