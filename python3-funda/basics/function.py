def sayHello(): 
    print("Hello From Function")

sayHello()    

def greet(name):
    return ("Hello " + name)
print(greet("Nitin"))

getName = lambda name: "Hello " + name
print(getName("Nirvan"))