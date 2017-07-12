# -*- coding: utf-8 -*-
"""
Created on Mon May  1 13:32:42 2017

@author: Jon
"""
"problem 5"
#prim_prod is the product of all primes from 1-20.
prim_prod=46189
#A is the multiplying factor of prim_prod to give solution.
#The solution must be A*prim_prod where A must be divisible by 18,16,15,14,12
A=180
#starting value of 180 since it is the LCM of 20 and 18.
#To improve efficiency could use the LCM of more numbers or a different pair. 
while bool(A%18==0)==False or bool(A%16==0)==False or bool(A%15==0)==False or bool(A%14==0)==False or bool(A%12==0)==False:
    A+=20 #If A_int is a multiple of 20 then using step of 20 would be most efficient.
print(A*prim_prod)
  