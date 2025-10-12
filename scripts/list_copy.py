# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:12:40 2018

lists: copying

@author: u0015831
"""
# this behavior is specific for any mutable data structure
v1=[1,2,3,4]
v2=v1
v2[2]=9
print("v1: ", v1)

# slicing notation 
v1=[1,2,3,4]
C=v1[:]
C[1]=11
print("v1: ", v1)

# use list function
v1=[1,2,3,4]
v2=list(v1)
v2[2]=9
print("v1: ", v1)

# use copy
v1=[1,2,3,4]
v2=v1.copy()
v2[2]=9
print("v1: ", v1)

# more layers
L1 = [1,2,3] 
L2 = [4,5,6]
L3 = [7,8,9]

Lbig = [L1,L2,L3]
LbigAlias = Lbig
LbigAlias2 = Lbig.copy()
LbigShallow = Lbig[:]

from copy import deepcopy
LbigDeep = deepcopy(Lbig)

L1[0] = 99    #changes first element of L1
print(LbigAlias)
print(LbigAlias2)
print(LbigShallow)
print(LbigDeep)
