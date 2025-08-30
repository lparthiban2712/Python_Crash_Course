from my_car import Car

my_car = Car('toyota', 'corolla', 2020)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank()


from my_car import Car, ElectricCar

my_electric_car = ElectricCar('toyota', 'corolla', 2020)
print(my_electric_car.get_descriptive_name())
my_electric_car.fill_gas_tank()

import my_car

my_new_car = my_car.Car('subaru', 'outback', 2019)
print(my_new_car.get_descriptive_name())    
my_new_car.fill_gas_tank()

from my_car import *

my_new_electric_car = my_car.ElectricCar('subaru', 'outback', 2019)
print(my_new_electric_car.get_descriptive_name())    
my_new_electric_car.fill_gas_tank()


from my_car import ElectricCar as EC

my_new_electric_car = EC('subaru', 'outback', 2019)
print(my_new_electric_car.get_descriptive_name())    
my_new_electric_car.fill_gas_tank()