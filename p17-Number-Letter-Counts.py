# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 21:51:49 2022

@author: willi
"""

#Project Euler p17 Number Letter Counts
#English spelling of the name of each number has a unique name for numbers 1 through twenty,
#Then a unique name for each power of ten, then a keyword for each exponential poer of ten,
#Such as 10^2 (hundred), 10^3 (thousand), this would almost be too mny edges cases for practicality
#However, that is the actual purpose of this challenge.



def intToEnglishStr(integer):
    #Currently only operates for cases up to 999999999, Throws error on negative numbers
    if integer < 0 :
        raise Exception("Unintended Negative Number: Integer is: " + str(integer))
        
    if integer == 0:
        return "zero"
    
    
    returnString = ''
    
    #Handles the Millions to Hundreds of Millions Position by recursively
    #calling function onto this triplet
    appendString = ''
    
    millionsTriplet = integer %1000000000 // 1000000
    
    if millionsTriplet != 0:
        appendString = " " + intToEnglishStr(millionsTriplet) + " million"
    returnString += appendString
    
    
    #Handles the Thousands to Hundreds of Thousands Position by recursively
    #calling function onto this triplet
    
    appendString = ''
    
    thousandsTriplet = integer %1000000 // 1000
    
    if thousandsTriplet != 0:
        appendString = " " + intToEnglishStr(thousandsTriplet) + " thousand"
    returnString += appendString
    
    #Handles the Hundreds Positions
    appendString = ''
    hundredsPlace = integer % 1000 // 100
    if hundredsPlace != 0:
        appendString = " " + digitToEnglishStr(hundredsPlace) + " hundred"
    returnString += appendString
    
    
    #Handles the Tens and Ones Position, including Teens Edge cases
    appendString = ''
    tensOnesPlace = integer % 100
    
    if tensOnesPlace == 0:
        appendString = ''
    
    elif 0 < tensOnesPlace <= 19:
        if tensOnesPlace <= 9:
            appendString = digitToEnglishStr(tensOnesPlace)
        else:
            appendString = teenToEnglishStr(tensOnesPlace)
    else:
        tensPlace = tensOnesPlace//10
        onesPlace = tensOnesPlace%10
        
        if onesPlace != 0:
            appendString = tensToEnglishStr(tensPlace) + "-" + digitToEnglishStr(onesPlace)
        else:
            appendString = tensToEnglishStr(tensPlace)
    
    
    #This is broken, test with input of 1000 TODO
    if returnString == '':
        returnString += appendString
    else:
        if appendString != '':
            returnString += " and " + appendString
        
    if returnString != '':
        return returnString.strip()
    else:
        raise Exception("Empty String Return for Name")
    
    

def digitToEnglishStr(digit):
    #returns cases for digits between 1 and 9 as those would be listed, if not input then throws exception
    if digit <= 0 or digit >= 10:
        raise Exception("Digit is outside bounds of 1-9. Digit is: " + str(digit))
        
    if digit == 1: return "one"
    elif digit == 2: return "two"
    elif digit == 3: return "three"
    elif digit == 4: return "four"
    elif digit == 5: return "five"
    elif digit == 6: return "six"
    elif digit == 7: return "seven"
    elif digit == 8: return "eight"
    elif digit == 9: return "nine"

def teenToEnglishStr(teen):
    #returns cases for teens between 10 and 19 as those would be listed, if not input then throws exception    
    if teen <= 9 or teen >= 20:
        raise Exception("Teen is outside bounds of 10-19. Teen is: " + str(teen))
    
    if teen == 10: return "ten"
    elif teen == 11: return "eleven"
    elif teen == 12: return "twelve"
    elif teen == 13: return "thirteen"
    elif teen == 14: return "fourteen"
    elif teen == 15: return "fifteen"
    elif teen == 16: return "sixteen"
    elif teen == 17: return "seventeen"
    elif teen == 18: return "eighteen"
    elif teen == 19: return "nineteen"

def tensToEnglishStr(tens):
    #returns cases for numbers in then tens place between 2 and 9 as those would be listed, if not input then throws exception
    if tens <= 1 or tens >= 10:
        raise Exception("Tens is outside bounds of 2-9. Tens is: " + str(tens))
        
    if tens == 2: return "twenty"
    elif tens == 3: return "thirty"
    elif tens == 4: return "forty"
    elif tens == 5: return "fifty"
    elif tens == 6: return "sixty"
    elif tens == 7: return "seventy"
    elif tens == 8: return "eighty"
    elif tens == 9: return "ninety"

if __name__=="__main__":
    
    a = 1
    b = 1000
    
    letterSum = 0
    
    for i in range(a,b+1):
        for char in intToEnglishStr(i):
            if char != ' ' and char != '-':
                letterSum += 1
    print(letterSum)