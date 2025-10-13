# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 09:56:22 2018

source: https://www2.cs.duke.edu/courses/spring18/compsci101

read the King James Bible 
count the number of characters
@author: u0015831
"""

import urllib.request
url = "https://www2.cs.duke.edu/csed/data/kjv10.txt"

f = urllib.request.urlopen(url)
st = f.read().decode('utf-8')
st = st.lower()
total = len(st)
print ("total # chars = ",total)
print ("total # z’s = ",st.count("z"))
for ch in "abcdefghijklmnopqrstuvwxyz":    	print (ch,st.count(ch))
