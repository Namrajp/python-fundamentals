fruits = ['Apples','Oranges','Grapes', 'Pears']
vegetables = ['Carrots', 'Broccoli', 'Spinach', 'Cauliflower']


def get_fruits():    return fruits
def get_vegetables():    return vegetables  
def get_all_produce():    return fruits + vegetables    
def add_fruit(fruit):    fruits.append(fruit)
def add_vegetable(vegetable):    vegetables.append(vegetable)
def clear_fruits():    fruits.clear()
def clear_vegetables():    vegetables.clear()
def clear_all_produce():    fruits.clear(); vegetables.clear()


def count_fruits():    return len(fruits)
def count_vegetables():    return len(vegetables)
def count_all_produce():    return len(fruits) + len(vegetables)
# def remove_fruit(fruit):    if fruit in fruits: fruits.remove(fruit)
# def remove_vegetable(vegetable):    if vegetable in vegetables: vegetables.remove(vegetable)


print("Fruits List:")
for fruit in fruits:
    print(f'- {fruit}')  