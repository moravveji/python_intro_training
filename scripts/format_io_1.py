# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:53:41 2018

source: https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
@author: u0015831
"""

print("Sammy ate {0:f} percent of a {1}!".format(75, "pizza"))
print("Sammy ate {0:6.2f} percent of a {1}!".format(75, "pizza"))
print("Sammy ate {0:x} percent of a {1}!".format(75, "pizza"))
print("Sammy ate {0:3d} percent of a {1}!".format(75, "pizza"))

for i in range(3,13):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))