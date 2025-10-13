# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:29:41 2019
source: http://rwet.decontextualize.com/book/functions/
example: 
    as standalone
    python ucfirst.py <sea_rose.txt 
    as module
>>> from ucfirst import ucfirst
>>>print ucfirst("my favorite first names are Gertrude, Jehosephat and Gary")
"""

def ucfirst(s):
  return s[0].upper() + s[1:]

if __name__ == '__main__':
  import sys
  for line in sys.stdin:
    line = line.strip()
    if len(line) > 0:
      print(ucfirst(line))
    else:
      print(line)