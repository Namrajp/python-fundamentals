add = lambda x,y: x + y
double = lambda val: 2 * val
yell = lambda str: str.upper() + "!!!"

add(1,2) # 3
double(5) # 10
yell("hello") # 'HELLO!!!'

add.__name__ # '<lambda>' 
add.__name__ == double.__name__ # True