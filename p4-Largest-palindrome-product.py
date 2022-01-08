#Project Euler p4

def palidromeCheck(n):
    numstring = str(n)
    reversedstring = numstring[::-1]
    return numstring==reversedstring


if __name__ == "__main__":
        
    digits = 3
    a = 0
    b = 0
    maxPalindrome = 0
    
    for i in range(((10)**(digits-1)),((10)**(digits))):
        for j in range(((10)**(digits-1)),((10)**(digits))):
            n=i*j
            if palidromeCheck(n):
                if maxPalindrome<n:
                    maxPalindrome = n
                    a=i
                    b=j
                       
    print(maxPalindrome)
    print(a)
    print(b)
