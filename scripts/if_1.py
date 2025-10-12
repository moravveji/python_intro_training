1# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:49:23 2018

Basic if statement

source: http://anh.cs.luc.edu/handsonPythonTutorial/ifstatements.html
@author: u0015831
"""
ipay = 0
weight = float(input("How many pounds does your suitcase weigh? "))
if weight > 50:
    print("There is a $25 charge for luggage that heavy.")
    ipay = 1
print("Thank you for your business.")

balance = float(input("Enter the balance on your account "))
if ipay == 1:
    balance = balance - 25
    if balance < 0:
        print("negative balance!")

print("Your balance is :", balance)
        