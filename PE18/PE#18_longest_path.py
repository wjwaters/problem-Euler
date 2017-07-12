# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:21:38 2017

@author: wjwaters
"""

"Problem 18"
"Greatest sum of path through triangle of numbers"

A=[75]
B=[95,64]
C=[17,47,82]
D=[18,35,87,10]
E=[20,4,82,47,65]
F=[19,1,23,75,3,34]
G=[88,2,77,73,7,63,67]
H=[99,65,4,28,6,16,70,92]
I=[41,41,26,56,83,40,80,70,33]
J=[41,48,72,33,47,32,37,16,94,29]
K=[53,71,44,65,25,43,91,52,97,51,14]
L=[70,11,33,28,77,73,17,78,39,68,17,57]
M=[91,71,52,38,17,14,91,43,58,50,27,29,48]
N=[63,66,4,68,89,53,67,30,73,16,69,87,40,31]
O=[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

Rows=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O]

"Trial-Nearest Neighbour"
sum=75
n=0
for i in Rows:
    if n-1>=0:
        if i[n-1]>=i[n] and i[n-1]>=i[n+1]: 
            sum+=i[n-1]
        elif i[n+1]>=i[n] and i[n+1]>=i[n-1]:
            sum+=i[n+1]
        else:
            sum+=i[n]
    elif n+1<=len(i)
        if i[n+1]>=i[n]:
            sum+=i[n+1]
        else: 
            sum+=i[n]
        
print(sum)