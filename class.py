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
        super().__init__(name, email, age)

        # self.name = name
        # self.email = email
        # self.age = age
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance
maya = Customer('jane09', 'jane@admin.com', 25)
print(maya.greeting())


class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"My name is {self.first_name} {self.last_name}"

    def likes(self, thing):
          return f"{self.first_name} likes {thing}!"

p = Person('Tim', 'Garcia')

# p.full_name() # My name is Tim Garcia
# p.likes("computers") # Tim likes computers!
print(p.full_name())
print(p.likes("computers"))

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        return f"{self.year} {self.make} {self.model}"
class Car(Vehicle):
    def __init__(self,make,model,year,doors):
        super().__init__(make,model,year)
        self.doors = doors
    def info(self):
        return f"{self.year} {self.make} {self.model} {self.doors}-doors"
       
car = Vehicle('Toyota','Corolla',2020)
print(car.info())  # 2020 Toyota Corolla

tesla = Car('Tesla','Model S',2022,4)
print(tesla.info())  # 2022 Tesla Model S

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
book = Book('1984','George Orwell',328)
print(book.description())  # '1984' by George Orwell, 328 pages         