# Tuples are immutable - cannot change its members
# Create tuple
fruits = ('Apples', 'Oranges','Grapes')
# fruits2 = tuple(('Apples', 'Oranges','Grapes')) # using constructor like lists

# Single value needs training comma
fruits2 = ('Apples',)

#print(fruits2, type(fruits2))

# Get values
#print(fruits[1])

# Can't change values
#fruits[0] = 'Pears'

# Delete tuple
del fruits2
#print(fruits2)

# Get length
#print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

# Delete
del fruits_set
