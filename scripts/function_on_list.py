# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 17:00:09 2018

function on list

source: http://www.cs.cornell.edu/courses/cs1110/2018sp/
"""


def add_one(the_list):
    """Adds 1 to every elt
    Pre: the_list is all numb."""
    for x in the_list:
        x = x+1

def add_one_bis(the_list):
    """Adds 1 to every elt
    Pre: the_list is all numb."""
    lenl = len(the_list)
    lll = list(range(lenl))
    for i in lll:
        the_list[i] = the_list[i]+1        
        
grades = [5,4,7]

add_one(grades)
print(grades)

add_one_bis(grades)
print(grades)
