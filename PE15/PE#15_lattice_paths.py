# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 10:34:17 2017

@author: wjwaters
"""

"Problem 15 - lattice path"
"Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner."
"what about a 20x20 grid? "

#Suppose it requires N moves to get from A(top left corner) to B(bottom right corner)
#If the grid is an n(across) x m(down) rectangle. 
#Then if N was written as a list of across (A's) and down (D's) it must always contain n x A's and m x D's.
# e.g. A,A,A,D,D,D or A,D,A,D,D,A etc. for a 3x3 grid. 
# Therefore the total number of possible paths can be given by (n+m)C(n). 

def binomial(n,k):
   """Compute n factorial by a direct multiplicative method."""
   if k > n-k: k = n-k  # Use symmetry of Pascal's triangle
   accum = 1
   for i in range(1,k+1):
      accum *= (n - (k - i))
      accum /= i
   return accum


a=int(input("Find the number of possible paths for rectangular lattice from top left to bottom right where only movements down or right are allowed. What are the dimensions of the lattice axb? a= "))
b=int(input("b= "))

num_paths=binomial(a+b,a)

print("The number of possible paths for an "+str(a)+" by "+str(b)+" rectangular lattice is "+str(num_paths))