# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:43:11 2022

@author: u0015831
"""

import isVow_script
import isVow_module


# call isVow the bad way
# the code in the script file is fully executed, also the test part
print('regular file')
print(isVow_script.isVow('i'))
print(isVow_script.isVow('y'))


# call isVow the right way
# only the function itself will be executed
print('name == main')
print(isVow_module.isVow('i'))
print(isVow_module.isVow('y'))