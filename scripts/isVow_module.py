# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:42:24 2022

source: https://sites.pitt.edu/~naraehan/python3/mbb20.html
@author: u0015831
"""


def isVow(char):
    return char.lower() in 'aeiou'

def main():
    print(isVow('i'))
    print(isVow('I'))
    print(isVow('K'))
	
if __name__ == '__main__':
    main()