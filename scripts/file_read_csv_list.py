# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:32:57 2019

source: https://www.alexkras.com/how-to-read-csv-file-in-python/
"""

import csv
with open('MOCK_DATA.csv') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = []
    for row in reader:
        data.append(row)