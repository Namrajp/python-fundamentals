from functools import wraps 

def perform_action(func):
    @wraps(func)
    def wrap_func():
        print("something is happening")
        return func()
    return wrap_func

@perform_action
def whisper():
    return "Shhhh"

@perform_action
def shout():
    return "WHOA!"

shout.__name__ # 'shout' - much better 

print(whisper())  # Output: something is happening \n Shhhh
print(shout())    # Output: something is happening \n WHOA! 
print(whisper.__name__)  # Output: whisper
print(shout.__name__)    # Output: shout