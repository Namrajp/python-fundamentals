with open('first.txt', 'w') as file:
    file.write('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eos molestias ea sit veniam, rerum, totam quis eaque excepturi aut, nostrum reiciendis. At, harum quos adipisci magni nesciunt aliquid beatae sit!')

with open('first.txt', 'r') as file:
    print(file.read())

with open('first.txt', 'r+') as file:
    file.write("\nI'm at the beginning\n")
    file.seek(100)
    file.write("\nI'm in the middle\n")
    file.seek(0)
    print(file.read())

with open('first.txt', 'a+') as file:
    file.write("\nI'm at the end\n")
    file.seek(0)
    print(file.read())

with open('first.txt', 'w+') as file:
    file.write("Now everything is overwritten :(")
    file.seek(0)
    print(file.read())