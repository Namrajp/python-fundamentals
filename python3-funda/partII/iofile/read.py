file = open('first.txt', 'r')

# type in the following commands

file.read() # we see all our test
file.read() # nothing now!

file.seek(0) # move the cursor back to the beginning
file.read() # there it is!

file.closed # False
file.close()
file.closed # True

file.read() # ValueError: I/O operation on closed file