# -*- coding: utf-8 -*-
"""
Spyder Editor

example for loop  from Python tutorial R 3.7.0
"""
words = ['cat', 'window', 'defenestrate']


for w in words[:]: # Loop over a slice copy of the entire list.
#for w in words: # Loop over the sequence, beware for an infinite list!.
   if len(w) > 6:
      words.insert(0, w)

print(words)