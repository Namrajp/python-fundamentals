import my_calculations
result_add = my_calculations.add(10, 5)
result_subtract = my_calculations.subtract(10, 5)
print("Addition Result:", result_add)
print("Subtraction Result:", result_subtract)




# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module pip install camelcase
from camelcase import CamelCase

# Import custom module pip install validator
import validator  
# from validator import validate_email  # pip install validate_email

from validate_email import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
# print(c.hump('hello there world'))

email = 'test#test.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Email is bad')