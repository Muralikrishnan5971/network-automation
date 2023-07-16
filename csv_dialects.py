import csv

csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')

with open('delimts.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, dialect='hashes', lineterminator='\n')
    writer.writerow((343, 'murali', 3431))