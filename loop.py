#ttps://github.com/bradtraversy/python_sandbox

# Simple for loop

people = ['Brad','Catalin','Siera','Megan']

# for person in people:
#     print(f'Current person: {person}')

# Break
# for person in people:
#     if person == 'Siera':
#         break
#     print(f'Current person: {person}')

# Continue
# for person in people:
#     if person == 'Siera':
#         continue
#     print(f'Current person: {person}')

# Range
# for i in range(len(people)):
#     print(people[i])

# for i in range(0, 11):
#     print(f'Number: {i}')

# while 
count =0
while count < 10:
    print(f'count: {count}')
    count += 1
y=1
while y<=5:
    print(y)
    y+=1    

for i in range(1,6):
    print(f'count: {i}')

users = ['Alice', 'Bob', 'Charlie', 'Diana']
for user in users:
    print(f'User: {user}')    

print("Using index to access users:")

for i in range((len(users))):
    print(f'Index {i} User: {users[i]}')
