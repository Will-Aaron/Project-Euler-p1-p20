# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:35:56 2021

@author: willi
"""
#Using the Pollard Rho Factorization Method
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

#This recursive function will find a factor of the input n
#If it is prime then the prime is included in a set of prime factors,
#If not then the factor and it's pair are broken down as well
def primeBreakdown(x,y,n,primeDict):
    a = factorFind(x,y,n)
    b = int(n/a)
    if b==1:
        if a in primeDict.keys():
            primeDict[a] += 1
        else:
            primeDict[a] = 1
    else:
        primeBreakdown(x,y,a,primeDict)
        primeBreakdown(x,y,b,primeDict)



if __name__ == "__main__":
    #Initializes parameters for Pollard Rho Factorization Method
    x,y = 2,2
    #Initializes things for finding triangular numbers
    m = 2
    Found = False
    while ~Found:
        T = m*(m+1)//2
        primeDict = {}
        primeBreakdown(x, y, T, primeDict)
        divisorCount = 1
        for expo in primeDict.values():
            divisorCount = divisorCount * (expo+1)
        #print('checking: '+str(T)+' Divisors: '+str(divisorCount))
        #time.sleep(5)
        if divisorCount >= 500:
            break
        m += 1
        
    print(T)
