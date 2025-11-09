from my_calculations import add, subtract

def calculate_numbers(a,b,fn):
    if fn == 'add':
        return add(a,b)
    elif fn == 'subtract':
        return subtract(a,b)

result = calculate_numbers(1, 4, 'add') 
print(result)
# this should work - we're able to access add from the my_calculations file!