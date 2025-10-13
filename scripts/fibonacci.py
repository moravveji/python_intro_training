# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:02:31 2019
taken from Marina von Steinkirch

@author: u0015831
"""

def fib_generator():
   a, b = 0, 1
   print(a, b)
   while True:
      print(b)
      yield b
      a, b = b, a+b

def fib(n):
    '''
    >>> fib(2)
    1
    >>> fib(5)
    5
    >>> fib(7)
    13
    '''
    if n < 3:
       return 1
    a, b = 0, 1
    count = 1
    while count < n:
       print(count)
       count += 1
       a, b = b, a+b
    return b


def fib_rec(n):
    '''
    >>> fib_rec(2)
    1
    >>> fib_rec(5)
    5
    >>> fib_rec(7)
    13
    '''
    if n < 3:
       return 1
    return fib_rec(n - 1) + fib_rec(n - 2)