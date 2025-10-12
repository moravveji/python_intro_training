# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:25:00 2018

source: http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
@author: u0015831
"""

fruitslist = ['banana', 'apple',  'mango']
ratios = [0.2, 0.3, 0.1, 0.4]
winelist = ['merlot', 'chenin', 'chardonnay', 'temperanillo', 'whatever']
for fruit, ratio, wine in zip(fruitslist, ratios, winelist):
    print('{}% {} more {}'.format(ratio * 100, fruit, wine))
