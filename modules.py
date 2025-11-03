# Threre are core python modules, pip package manager

# import math
from math import pi, sqrt

# print(math.sqrt(16))
print(sqrt(81))


import math as m
print(m.pi) # Access using the alias 'm'

import my_calculations
result_add = my_calculations.add(10, 5)
result_subtract = my_calculations.subtract(10, 5)
print("Addition Result:", result_add)
print("Subtraction Result:", result_subtract)
