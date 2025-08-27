dimensions=(200,20)
print(dimensions)
print(dimensions[0])
print(dimensions[1])


print("*********************")

for dimension in dimensions:
    print(dimension)

print("*********************")
my_t=(3,)
print(my_t)

print("*********************")
# dimensions[0]=100 TypeError: Tuple does not support item assignment
dimensions=(300,30) # But re-assignation is possible
print(dimensions)