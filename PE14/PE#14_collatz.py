# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 13:54:56 2017

@author: Jon
"""

"Problem 14 - Collatz"

#takes a minute or so to compute but could be optimised using an empty array to store the length of sequnce for preceeding numbers.

m=int(input("Find the largest collatz sequence for numbers under m? m= "))
n_max=1
counter_max=0


for n in range(2,m):
    counter=0
    number=n
    while (n!=1):
        if (n%2==0):
            n=n/2
            counter+=1
        else:
            n=3*n+1
            counter+=1
    if (counter>counter_max):
        n_max=number
        counter_max=counter
        
print("The longest collatz sequence for numbers under "+str(m)+" is "+str(counter_max)+" corresponding to number "+str(n_max))