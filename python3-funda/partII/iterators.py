str = "hello"
str_iter = iter(str)
# next(str_iter) # h
# next(str_iter) # e
# next(str_iter) # l
# next(str_iter) # l
# next(str_iter) # o
#next(str_iter) # StopIteration Error!

print(next(str_iter)) # This will raise StopIteration Error!
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))