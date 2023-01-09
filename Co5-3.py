#Pgm to read each row from a given csv file and print a list of strings

import csv

#Open the CSV file

with open("Hello.csv",'r')as file:
    # Create a CSV reader
    reader=csv.reader(file)

    #iterate over the rows of the  CSV fILE
    for row in reader:
       #Print the row as a list of strings
       print(row)
