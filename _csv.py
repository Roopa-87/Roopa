import csv
#file=open('sample',csv,'a')
with open('sample.csv','a',newline='')as file:
      record=csv.writer(file)
      record.writerow([9,'roopa',5])