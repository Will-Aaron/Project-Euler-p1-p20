# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 19:37:25 2021
Purpose of this code is to find the m-th prime
@author: willi
"""

import math

#This function will return a found factor or if the number is prime
#it will just return the prime number
def factorFind(x,y,n):
    d = 1
    while d==1:
        x = ((x^2)+1)%n
        y = (((((y^2)+1)%n)^2)+1)%n
        d = math.gcd(abs(x-y),n)
    return d


if __name__=="__main__":
        
    #Initializes parameters for Pollard Rho Factorization Method
    x,y = 2,2
    
    primeCount = 0
    
    p = 0
    
    n = 2
    
    m = 10001
    
    while primeCount != m:
        if factorFind(x,y,n) == n:
            p = n
            primeCount += 1
        n += 1
        
    print(p)