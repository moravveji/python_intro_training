# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:35:22 2019

source: https://www.alexkras.com/how-to-read-csv-file-in-python/

"""

import csv
with open('MOCK_DATA.csv') as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]
    
print('type(data): ', type(data))
print(data[0]['id'])