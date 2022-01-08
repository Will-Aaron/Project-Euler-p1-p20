#sum all even fibonacci numbers below 4 million together
#fibonacci sequence starting with 1,1 will hold the pattern odd, odd, even,...


if __name__=="__main__":
    
    n = 4000000 #Stopping Point
    
    #Initializes Summation Loop
    a = 1
    b = 1
    F = a+b
    summand = 0
    
    while F < n:
        #Includes even term in summation
        summand += F
        #Sets up next even term
        a = F+b
        b = a+F
        F = a+b
    
    print(summand)
