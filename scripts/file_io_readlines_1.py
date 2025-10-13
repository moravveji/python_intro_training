# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:45:37 2019

@author: taken from http://www2.hawaii.edu/~takebaya/cent110/file_in/file_in.html
"""

infile = open("students.txt","r")
lines = infile.readlines()
infile.close()
for line in lines:
    tokens = line.split(",")
    total = 0
    for i in range(1, len(tokens)):
        total = total + float(tokens[i])
    average = total/(len(tokens) - 1)
    print(tokens[0],"has an average of: ",average)