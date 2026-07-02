import time
# epoch --> a date and time from which a computer measures system time

#print(time.ctime(1000)) 
# the ctime method will convert a time expressed in seconds since epoch to a readable string.
# epoch --> whgen your computer thinks time began (reference point)


# print(time.time())
# returns current seconds since epoch

# retrive current date and time
print(time.ctime(time.time()))

# another way to get current date and time:
time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B %D %Y %H %M %S", time_object)
# %B --> name of the month
# %D --> day
# %Y --> for the year
# %H --> for hour
# %M --> for minutes
# %S --> for seconds

print(local_time)

print("--------------------------------------------------")

time_string = "20 April 2020"
time_object = time.strptime(time_string, "%d %B %Y")
print(time_object)

# (year, month day, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)