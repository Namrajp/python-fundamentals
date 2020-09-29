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
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
maya = Customer('jane09')


