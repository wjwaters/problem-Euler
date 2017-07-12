# -*- coding: utf-8 -*-
"""
Created on Tue May 23 14:21:34 2017

@author: wjwaters
"""

"Problem 8"
"The largest product of n adjacent numbers in a series of numbers"

#Reading in a large number into a matrix.
with open('PE8.txt') as f:
    M = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(a) for a in line]
            M.append(line)
#flattens the list to a 1D array    
flat_M = [val for sublist in M for val in sublist]
#N=123456789
n=13
#n is number of consecutive numbers to multiply in list
#series=str(N)
product_temp=1
product=1

for j in range(0,len(flat_M)-n+1):
    product_temp=1
    for i in range(0,n):
        digit=int(flat_M[i+j])
        product_temp*=digit    
    if product_temp>product:
        product=product_temp
print("the largest product of "+str(n)+" numbers in the series is "+str(product))






