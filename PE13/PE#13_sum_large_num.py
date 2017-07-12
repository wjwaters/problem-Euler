# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:08:34 2017

@author: Jon
"""

"PE#13-Large sum"

total=0

with open('PE13.txt') as f:
    M = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(a) for a in line]
            M.append(line)
            
for i in range(100):
    N=M[i]
    total+=N[0]
    
ts=str(total)
t_lead_s=ts[0]
for j in range(1,10):
    t_lead_s+=ts[j]
    
t_lead_int=int(t_lead_s)
    
    
    
    
print("The first 10 digits of the sum of lines in PE12.txt is: "+str(t_lead_int))