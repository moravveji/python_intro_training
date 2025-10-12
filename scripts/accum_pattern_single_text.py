# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:02:14 2019

@author: http://ice-web.cc.gatech.edu/ce21/1/static/audio/static/pip/Dictionaries/dictionary_accum.html#scarlet.txt
"""

#f = open('study_in_scarlet.txt', 'r', encoding="utf8")
f = open('Data\patients.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 #initialize the accumulator variable

# check the number of occurences of t
for ch in txt:
   if ch == 't':
      t_count = t_count + 1   #increment the counter
print("t: " + str(t_count) + " occurrences")
f.close()


# a more elaborted loop for 2 characters
# a lot of elif's required to test for all 26 characters
t_count = 0 #initialize the accumulator variable
s_count = 0 # initialize the s counter accumulator as well
for ch in txt:
   if ch == 't':
      t_count = t_count + 1   #increment the t counter
   elif ch == 's':
      s_count = s_count + 1
print("t: " + str(t_count) + " occurrences")
print("s: " + str(s_count) + " occurrences")
f.close()
