 # -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:11:59 2019

@author: http://ice-web.cc.gatech.edu/ce21/1/static/audio/static/pip/Dictionaries/dictionary_accum.html#scarlet.txt
"""

f = open('study_in_scarlet.txt', 'r', encoding='utf8')
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

# build a second dictionary, containing the scrabble scores for individual characters
# calculate the scrabble score of your text
letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, '':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}

tot = 0
for y in x:
   if y in letter_values:
      tot = tot + letter_values[y] * x[y]

print('total scrabble score = ', tot)
