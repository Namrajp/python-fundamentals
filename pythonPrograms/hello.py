from sys import argv

def main():
	if ((len(argv)) == 2):
		hello(argv[1])

	else:
		print("invalid number of arguments.")
	
def hello(s):
	print(f"hello, {s}")


if __name__ == "__main__":
	main()


