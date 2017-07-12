# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:09:45 2017

@author: wjwaters
"""

"Problem 10 - Sum of primes"

n=int(input("This code calculates the sum of primes below n, what value of n would you like? n= "))
#start counter at 2 which includes 2 and 3 as the first primes. 

prime=3
prime_sum=5
primes=[2,3]

#keep computing untill counter reaches the nth prime
while prime<n-1:
    prime+=2
    #skips even numbers.
    check_if_prime = (not prime%div==0 for div in primes)
    #compute this for loop, if every result is true.
    #only checking for prime divisors i.e. only values in list: primes.
    if all(check_if_prime)==True:
       #print(str(prime)+" is prime")
       prime_sum+=prime
       if prime<=n/3:
           primes.append(prime)
       #add the prime to the list of primes already collected.

print("the sum of primes below " +str(n)+" is "+str(prime_sum))  