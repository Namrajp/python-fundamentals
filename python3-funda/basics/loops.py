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