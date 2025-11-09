name = 'Nawaraj'
age = 43

mystring = 'Hello World!'

print(name.upper())
print(mystring.capitalize())


print(mystring.replace('World', name))
print(f'My name is {name} and I am {age} years old.')
print('My name is %s and I am %d years old.' % (name, age))
print('My name is {} and I am {} years old.'.format(name, age))

print(mystring.split())
print(mystring.find('o'))
print(mystring.count('l'))  