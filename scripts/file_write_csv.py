# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:43:58 2019

https://www.tutorialspoint.com/reading-and-writing-csv-file-using-python
"""

# use writerow
import csv
csvData = [('Peter', '22'), ('Jasmine', '21'), ('Sam', '24')]
csvFile = open('person.csv', 'w', newline='')
obj=csv.writer(csvFile)

for person in csvData:
    obj.writerow(person)
    
csvFile.close()

#use writerows
csvfile = open('persons_bis.csv','w', newline='')
obj = csv.writer(csvfile)
obj.writerows(csvData)
csvFile.close()
