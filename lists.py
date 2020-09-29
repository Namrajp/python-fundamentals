# Alist is a Colledtion which is  ordered and changaable.Allows duplicate members
# Create List
numbers = [1,3,2,4,5]
fruits = ['Apples','Oranges','Grapes', 'Pears']

# Use of Constructor
# numbers2 = list((1,3,2,4,5,7))

# print(fruits[1])

# Get length
# print(len(fruits))

# Append to list
fruits.append('Mangoes')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Change values
fruits[2] = 'blueberries'

# Remove with pop
fruits.pop(2)

# Revese the list
fruits.reverse()


# Sort List
fruits.sort()
fruits.sort(reverse=True)  # reverse sort

print(fruits)
