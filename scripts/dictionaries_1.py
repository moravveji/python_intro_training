# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:58:30 2018

dictionaries

@author: u0015831
"""

#A few examples of a dictionary

#First way to setup a dictionary
zipdict = {}

#Add a couple of cities to the dictionary
zipdict['Heverlee'] = 3001
zipdict['Leuven'] = 3000
zipdict['Brussel'] = 1000
zipdict['Gent'] = 9000

# another way
zipdict.update({'Antwerpen': 2000, 'Brugge': 8000})

#Use the function key() - 
if 'Gent' in zipdict:
    print('Gent is in the dictionary. ZIP: ', zipdict['Gent'])
else:
    print('Gent is not in the dictionary')

#Use the function keys() - 
keys = zipdict.keys()
print(keys)
#keys.sort() will this work?
#print(keys)

# List of codes in a list:
values = zipdict.values()
print(values)
#values.sort()
#print(values)

