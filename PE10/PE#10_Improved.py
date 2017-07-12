# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"PE#10 IMPROVED"
n=int(input("This code calculates the sum of primes below n, what value of n would you like? n= "))
#create empty vector with n elements
vect = [0] * n
prime = 3
sum_of_primes = 2
#while loop up to n
while prime < n:
    #if the element of vect corresponding to the value of the prime=0 it must not be a multiple of previous primes
    if vect[prime] == 0:
        sum_of_primes += prime
        i = prime
        #while loop changes every multiple of prime into a non zero entry in vect
        while i < n:
            vect[i] = 1
            i += prime
    #skip even numbers
    prime += 2

print("the sum of primes below " +str(n)+" is "+str(sum_of_primes)) 