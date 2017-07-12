# -*- coding: utf-8 -*-
"""
Created on Tue May 23 12:59:38 2017

@author: wjwaters
"""

"Problem 7"

"Find the value of the nth prime"

n=int(input("Which prime would you like to find? n= "))
#start counter at 2 which includes 2 and 3 as the first primes. 
counter=2
prime=3

#keep computing untill counter reaches the nth prime
while counter<=n-1:
    prime+=2
    #stop cuts computation time by dividing by only the values less than half 
    stop=1+prime//2
    check_if_prime = (not prime%div==0 for div in range(3,stop,2))
    #compute this for loop, if every result is true i.e. not divisible then add counter
    if all(check_if_prime)==True:
       #print(str(prime)+" is prime")
       counter+=1
       
    #else:
        #print(str(prime)+" is NOT prime")
    
print("the " +str(n)+"th prime is "+str(prime))       
     