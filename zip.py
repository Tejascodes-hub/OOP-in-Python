# zip(*iterables) = agreegate elements from two or more iterables (list, tuples, sets, etc.)
# create a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ["p@ssword", "abc123", "guest"]

users = dict(zip(usernames, passwords))

for key, value in users.item():
    print(key+ " "+value)