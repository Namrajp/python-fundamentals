with open('newfile.csv', 'a') as csvfile:
    data = ['name', 'fav_topic']
    writer = csv.DictWriter(csvfile, fieldnames=data)
    writer.writeheader() # this writes the first row with the column headings
    writer.writerow({
        'name': 'Elie',
        'fav_topic': 'Writing to CSVs!'     
    }) 