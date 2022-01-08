#Find sum of all multiples of 3 or 5 below 1000
#Solution to problem 1 of Project Euler Problems


if __name__ == "__main__":
    
    #Determines Parameters of our problem
    n = 1000 #Upper bound of numbers to check
    a = 3 #First Multiple
    b = 5 #Second Multiple
    c = a*b
    
    multA = (n-1)//a # Number of multiples of "a" below "n"
    multB = (n-1)//b # Number of multiples of "b" below "n"
    multAB = (n-1)//c # Number of multiples of both "a" and "b" below "n"
    
    summand = 0
    
    #print(multA)
    #print(multB)
    #print(multAB)
    
    for i in range(1,multA+1):
        summand += a*i
    for j in range(1,multB+1):
        summand += b*j
    for k in range(1,multAB+1):
        summand -= c*k
    
    print(summand)
