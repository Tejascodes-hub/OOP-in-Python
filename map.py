# map() = applies a function to each item in an iterable (list, tuple, etc.)

# map function accepts two arguments :
# map(function, iterable) 

store = [("shirt", 25.00),
         ("jeans", 20.00),
         ("jacket", 35.00)]

# we'll convert these dollar rate to euros:
to_euros = lambda data:(data[0], data[1] * 0.88)

# we'll convert euros to dollar:
to_dollars = lambda data: (data[0], data[1] / 0.88)
store_euros = list(map(to_euros, store))
# here --> (to_euros) is a function & (store) is a iterable.

for i in store_euros:
    print(i)

store_dollar = map(to_dollars, store)
for i in store_dollar:
    print(i)