# Dictionary is collection of name value pair,similar to objects in js

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

#print(person, type(person))

# Use constructor
person2 = dict(first_name='Sara', last_name='Williams')
#print(person2, type(person2))

# Get value

#print(person['first_name'])
#print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-555'

# Get dict keys
# print(person.keys())

# Get dict items

#print(person.items())
#print(person.keys())

# Copy dict         is similar to spread in js
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item 
del(person['age'])
person.pop('phone')

# Clear
person.clear()
print(person)

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Nitin', 'age': 3},
    {'name': 'Nirvan', 'age': 1}
]
print(people[1]['age'])