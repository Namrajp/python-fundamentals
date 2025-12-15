# from sys import argv

def main():
	name = input("What's your name? ")

	# truthiness check and boolean check are not same if name != False is boolean check not valid
	if name:
		hello(name)
	else:
		hello()
	
	
def hello(to="world"):
	print(f"hello, {to}")

if __name__ == "__main__":
	main()

