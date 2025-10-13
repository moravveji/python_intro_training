
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:29:17 2019

source: https://www.journaldev.com/22439/python-namedtuple
"""

from collections import namedtuple

Employee = namedtuple('Employee', ['name', 'age', 'role'])

# below are also valid ways to namedtuple
# Employee = namedtuple('Employee', 'name age role')

emp1 = Employee('Pankaj', 35, 'Editor')
emp2 = Employee(name='David', age=40, role='Author')

for p in [emp1, emp2]:
    print(p)


# accessing via name of the field
for p in [emp1, emp2]:
    print(p.name, 'is a', p.age, 'years old working as', p.role)