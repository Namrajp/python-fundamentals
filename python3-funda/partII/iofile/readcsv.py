import csv

with open('file.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    rows = list(reader)
    for row in rows:
        print(', '.join(row))

# name, type, age
# Whiskey, dog, 3
# Moxie, cat, 7
# Mascis, dog, 2