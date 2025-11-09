import helper

print("I'm from the other file!")

helper.display(__name__)  

if __name__ == '__main__':
  print("I'm the other file and was loaded directly!")