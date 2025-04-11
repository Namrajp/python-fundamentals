def cube(number):
    return number * number * number
result = cube(5)    
print(result)


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3 and num2 >= num1:
        return num2
    else:
        return num3
print(max_num(40, 2, 100))                












