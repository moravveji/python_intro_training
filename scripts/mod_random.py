# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:11:32 2018

some examples on random module
@author: u0015831
"""
# import the module
import random

# good practice to use the seed function, and timing data as an argument for it.
from datetime import datetime
random.seed(datetime.now())

print(random.random())
print(random.random())

print(random.uniform(10, 14))

random.randint(1, 100)
random.randint(1, 100)
random.randint(1, 100)
random.randint(1, 100)

ls = [1, 2, 88, 92, 10, 3, 127]
print(random.choice(ls))
print(random.choice(ls))

print(random.randrange(1,33))
print(random.randrange(1,33))
print(random.randrange(1,33))

print(ls)
print(random.shuffle(ls))
print(ls)