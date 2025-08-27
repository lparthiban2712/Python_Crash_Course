bikes=['ducati', 'honda', 'yamaha', 'suzuki']
del bikes[0]
# del bikes["yamaha"] TypeError: list indices must be integer or slice, not str
print(bikes)
popped_bike=bikes.pop() #removes and returns last item from the list
print(popped_bike)
print(bikes)
# removed_bike=bikes.remove("honda") # Returns None, so no use of storing into an variable
# print(removed_bike)
print(bikes)
bikes.append("access")
bikes.append("activa")
print(bikes)
popped_bike=bikes.pop(2)
print(popped_bike)
print(bikes)
# bikes.remove() needs one argument
print(bikes)
# print(bikes[3]) IndexError: list index out of range