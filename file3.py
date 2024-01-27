import csv
#file=open('sample.csv','w')
with open('sample.csv','w')as file:
    data=[
        [1,'roopa'],
        [2,'pandu'],
        [3,'kaveri'],
    ]
    record=csv.writer(file)
    record.writerows(data)
