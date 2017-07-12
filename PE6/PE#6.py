# -*- coding: utf-8 -*-
"""
Created on Mon May 15 12:42:20 2017

@author: Jon
"""

"Problem 6"

sum_sq=0
tot=0

#sum the square from 1-100
for a in range(101):
    sq=a*a
    sum_sq+=sq
#sum numbers 1-100
for b in range(101):
    tot+=b

print(tot*tot-sum_sq)