# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:54:15 2017

@author: Jon
"""

"Problem 4"
#c_large could be set to any 'small' number. 100*101=10100.
c_large=10100
#cycle through values of a and b in reverse from 999. Test with C. 
for a in range(999,100,-1):
    for b in range(999,100,-1):
        C=str(a*b)
#The test: since C now a string c[::-1] represents full string in reverse.
        if bool(C[::1]==C[::-1])==True:
            c_temp=int(C)
            if c_temp>c_large:
                c_large=c_temp
                
print(c_large)
            
            

   
        