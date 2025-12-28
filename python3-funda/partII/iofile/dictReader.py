import csv

with open('file.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    rows = list(reader)
    for row in rows:
        print(row)

# {'age': '3', 'name': 'Whiskey', 'type': 'dog'}
# {'age': '7', 'name': 'Moxie', 'type': 'cat'}
# {'age': '2', 'name': 'Mascis', 'type': 'dog'}  