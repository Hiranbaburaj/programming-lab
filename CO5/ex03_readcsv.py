import csv
with open('example3.csv', newline='') as csvfile:
 data = csv.reader(csvfile)
 for row in data:
   print(row)
