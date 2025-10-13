# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:56:59 2019
source: https://pythonbasics.org/multiple-return/
@author: u0015831
"""

def getPerson():
    name = "Leona"
    age = 35
    country = "UK"
    return name,age,country

name,age,country = getPerson()
print(name)
print(age)
print(country)