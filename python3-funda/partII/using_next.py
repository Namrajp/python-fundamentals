def use_next():
    for x in range(10):
        yield x

gen = use_next()
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 2