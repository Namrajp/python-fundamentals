# A classs i like a blueprint for creating objects. An object has properties and methods (functions) associated with it. Almost everything in Python is an object
# Create class
 
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is  {self.name} and I am {self.age}.'
    
    def has_birthday(self):
        self.age +=1
# Init user object
namraj = User('Namraj Pudasaini', 'namraj@gmail.com',37)

namraj.has_birthday()
print(namraj.greeting())

# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age, balance=100):
        self.name = name
        self.email = email
        self.age = age
        self.balance = balance
maya = Customer('jane09', 'jane@austin.yahoo.com', 25, 500)

print(maya.name, maya.balance)
print(isinstance(maya, User))  # True
print(issubclass(Customer, User))  # True
print(maya.greeting())

class Toy():

    count = 1

    def __init__(self,name):
        self.name = name
        self.id = Toy.count
        Toy.count += 1

duplo = Toy(name='duplo')
lego = Toy(name='lego')
knex = Toy(name='knex')        

print(duplo.id)
print(lego.id)
toys = [duplo,lego,knex]
for toy in toys:
    if toy.id == 2:
        found_toy = toy
print(found_toy.name)