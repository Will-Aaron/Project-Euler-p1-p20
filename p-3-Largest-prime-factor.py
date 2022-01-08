#Project Euler p3
#Find the Largest Prime Factor
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
def primeBreakdown(x,y,n,setFactors):
    a = factorFind(x,y,n)
    b = int(n/a)
    if b==1:
        setFactors.add(a)
    else:
        primeBreakdown(x,y,a,setFactors)
        primeBreakdown(x,y,b,setFactors)

if __name__=="__main__":
    n = 600851475143
    
    setFactors = set()
    x,y = 2,2
    
    primeBreakdown(x,y,n,setFactors)
    print(setFactors)
    print(max(setFactors))
    
    

