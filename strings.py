name = "Namraj"
age = 37

# Concatenate
# print('Hello, my name is ' + name + ' I am ' + str(age) )

# Arguments by Position
#print('Hello, my name is {name} and I am {age}'.format(name=name, age=age) )
print('My name is %s and I am %d years old.' % (name, age))

# F-Strings  (3.6+) 
print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize 
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))
print(s.replace('world','everyone'))

sub = 'h'
print(s.count(sub))

# Split into a list
print(s.split())

# Starts with
print(s.startswith('hello'))
print(s.endswith('d'))

# Find Position 
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())
