import csv
with open('example3.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 for row in data:
   print(row['Company'])
