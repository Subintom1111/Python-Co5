# Program to read specific columns of a given CSV file and print the content

import csv

# specify the column indices that you want to read
# e.g. column 0 is the first column, column 1 is the second column, etc.
columns_to_read = [0, 2]

# open the CSV file and read the contents
with open('Helloss.csv', 'r') as f:
   clmn_reader = csv.reader(f)

# iterate over the rows of the CSV
   for row in clmn_reader:
# print the contents of the specified columns
       print([row[i] for i in columns_to_read])