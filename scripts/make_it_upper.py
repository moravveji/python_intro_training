# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:12:22 2019
source: http://rwet.decontextualize.com/book/functions/
example: python make_it_upper.py <sea_rose.txt 
"""

import sys

def ucfirst(s):
  return s[0].upper() + s[1:]

for line in sys.stdin:
  line = line.strip()
  if len(line) > 0:
    print(ucfirst(line))
  else:
    print(line)