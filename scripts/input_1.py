# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 14:22:32 2018

source: https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html
@author: u0015831
"""

name = input('Enter your name: ')
print('Hello ' + name + '!')
print(type(name))
age = input('Enter your age: ')
print(age)
print(type(age))

#use typecasting
xString = input("Enter a number: ")
x = float(xString)
yString = input("Enter a second number: ")
y = float(yString)
print('The sum of ', x, ' and ', y, ' is ', x+y, '.')