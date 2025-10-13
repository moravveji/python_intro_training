h# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:31:20 2019

@author: http://ice-web.cc.gatech.edu/ce21/1/static/audio/static/pip/Dictionaries/dictionary_accum.html#scarlet.txt
"""

f = open('study_in_scarlet.txt', 'r', encoding="utf8")
txt = f.read()
f.close()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
for c in txt:
   if c not in x:
      # we have not seen this character before, so initialize a counter for it
      x[c] = 0

   #whether we've seen it before or not, increment its counter
   x[c] = x[c] + 1

for c in x.keys():
   print(c + ": " + str(x[c]) + " occurrences")