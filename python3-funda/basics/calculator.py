x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x+y)
div = round(x/y, 4); # rounds to 4 decimal places

print(f"Sum: {z:0.3f}") # rounds to 3 decimal places
print(f"div: {div}")

print(f"Sum: {z:,}")  # comma adds in large integers seperates 10 times places with ,


