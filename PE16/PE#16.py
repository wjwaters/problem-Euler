# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 12:50:10 2017

@author: wjwaters
"""

"Problem 16"

"sum of 2^1000"

import time
 
def pow2sum(exp):
    pow = list(str(2**1000))
    return sum([int(i) for i in pow])
 
start = time.time()
n = pow2sum(1000)
elapsed = (time.time() - start)
print (str(n)+" found in "+str(elapsed)+" seconds.")