p# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:07:12 2018

@author: u0015831
"""

import matlab.engine
eng = matlab.engine.start_matlab()
eng.triarea(nargout=0)