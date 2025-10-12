# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 10:09:14 2019

@author: taken from http://www2.hawaii.edu/~takebaya/cent110/file_in/file_in.html
"""

infile = open("students_header.txt","r")
line1 = infile.readline()
lines = infile.readlines()
infile.close()
outfile = open("data.html","w")
outfile.write("<html>\n  <body>\n")
outfile.write('    <table border="1">\n')
outfile.write('      <tr>\n')
headers = line1.strip().split(",")
outfile.write('        ')
for header in headers:
    outfile.write('<td>' + header + '</td> ')
outfile.write('\n      </tr>\n')
for line in lines:
    tokens = line.strip().split(",")
    outfile.write('      <tr>\n')
    outfile.write('        ')
    for token in tokens:
        outfile.write('<td>' + token + '</td> ')
    outfile.write('\n      </tr>\n')
outfile.write('    </table>\n')
outfile.write('  </body>\n</html>')
outfile.close()