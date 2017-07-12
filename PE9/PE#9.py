# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:02:43 2017

@author: Jon
"""

"Problem 9"

Test=0

while Test==0:
    for a in range(1,500,1):
        for b in range(1,500,1):
            temp=a+b+(a**2+b**2)**(.5)
            if temp==1000:
                Test=1
                a_final=a
                b_final=b
                c_final=(a**2+b**2)**(.5)
                
product=a_final*b_final*c_final
print("The product of the only pythagorean triple whose sum equals 1000 is: "+str(product))
print(a_final)
print(b_final)
print(c_final)