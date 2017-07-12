# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:03:51 2017

@author: Jon
"""

"Special triangle numbers"

n=int(input("Find the first triangle number with n factors? n= "))
tri_num=0

#Generic large number in range, break stops when condition is met so not important. Could use while loop instead, it would be more genral.
for i in range(100000000000):
    count=0
    tri_num+=i
    if tri_num>n:
        for j in range(1,int(tri_num**0.5)):
            #check divisibility from 1 to sqrt(tri) since factors arisw in pairs. i.e.counter+2.
            if tri_num%j==0:
                count+=2
        if count>n:
            break
print("The first triangle number with over "+ str(n) +" factors is: "+str(tri_num))