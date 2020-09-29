# boolean if elif else

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("YOu are a short male")   
elif not(is_male) and is_tall:
    print("You are not a male and you are tall")     
else :
    print("You are not tall and you are not male")    