def gensquares(n):
    for num in range(n):
        yield num**2

for x in gensquares(10):
    print(x)