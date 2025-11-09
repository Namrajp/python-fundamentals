# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person['first_name'])
print(person['last_name'])
# print(person.age)
print(person.get('age'))
print(person.get('address', 'Not Found'))
print(person)
print(len(person))
print(type(person))
# print(person.first_name)

# List of dict
people = [
    {'name': 'Nitin', 'age': 'Eighteen'},
    {'name': 'Nirvan', 'age': 1}
]
print(people[0]['age'])
print(people[1]['age'])