# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:51:15 2019
taken from Marina von Steinkirch

@author: u0015831
"""

def convert_to_decimal(number, base):
   multiplier, result = 1, 0
   while number > 0:
      result += number%10*multiplier
      multiplier *= base
      number = number//10
   return result

def test_convert_to_decimal():
   number, base = 1001, 2
   print ('number = ', number)
   print ('base = ', base)
   assert(convert_to_decimal(number, base) == 9), 'result must equal 9'
   
