import csv
#Data to be inserted
data=[{'Name':'Iphone','Age':20,'State':'Kerala'},
      {'Name':'Oneplus','Age':7,'State':'Karnataka'},
      {'Name':'Realme','Age':5,'State':'Tamil Nadu'},]

#Write to CSV file
with open('Hellos.csv','w') as csvfile:
      headernames=['Name','Age','State']
      csvwriter=csv.DictWriter(csvfile,fieldnames=headernames)
      csvwriter.writeheader()
      for row in data:
          csvwriter.writerow(row)

#Read from CSV file and print contentsZ
with open('Hellos.csv','r') as csvfile:
      reader=csv.DictReader(csvfile)
      for row in reader:
          print(row)