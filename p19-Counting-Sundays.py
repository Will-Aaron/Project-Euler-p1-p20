# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:05:13 2022

@author: willi
"""

#Project Euler Problem 19

#Initializations
#Not the most efficient way to do this and doesn't future proof for days before 1900, but easy to understand
monthName = {"January":0,
             "Feburary":1,
             "March":2,
             "April":3,
             "May":4,
             "June":5,
             "July":6,
             "August":7,
             "September":8,
             "October":9,
             "November":10,
             "December":11}

monthDayCount = {0:31,
                 1:28,
                 2:31,
                 3:30,
                 4:31,
                 5:30,
                 6:31,
                 7:31,
                 8:30,
                 9:31,
                 10:30,
                 11:31}
    
monthDayCountLeap = {0:31,
                     1:29,
                     2:31,
                     3:30,
                     4:31,
                     5:30,
                     6:31,
                     7:31,
                     8:30,
                     9:31,
                     10:30,
                     11:31}

dayName = {0:"Monday",
           1:"Tuesday",
           2:"Wednesday",
           3:"Thursday",
           4:"Friday",
           5:"Saturday",
           6:"Sunday"}

#Convention is to index days and months starting at zero, so the last day of january(january 31st) would be
#january day = 30. And by convention days' are given numbers counting from day 0 which is january 1st 1900 monday.

#given 365 days in a year, indexing at 0, the last day would be dayNum = 364
    
#given year, it find our if it's a leap year or not
def isLeapYear(year):
    if year%4 == 0:
        #If divisible by 4 then it's a leap year
        if year%100 == 0:
            #But if it's on a century, it won't be a leap year unless it's divisible by 400
            if year%400 == 0:
                return True
            return False
        return True
    return False

#TODO Given date, find day number indexing from day 0 with january 1st 1900. Frankly this is wha
#We really need for the challenge, the other function won't solve it. Cause given two days, we just need to find number of days between them mod 7
#Then use that and the starting day to figure out how many sundays passed

def dateToDayNum(month, day, year):
    
    dayNum = 0 #Initialization
    
    #check that the month number exists
    if month>11 or month<0:
        raise Exception("Month number does not exist. Month: " + str(month))
    
    
    #check that it doesn't exceed the number of days in the month, or if it's a negative day
    if day > monthDayCount[month] or day < 0:
        raise Exception("Day exceeds day count of month. Day: "+ str(day) + " Month: " + str(month) + " Day Count: " +str(monthDayCount[month]))
    
    
    #check that we work with a year after 1900
    if year < 1900:
        raise Exception("Year earlier than 1900. Year: "+str(year))
    
    #add days from start of year of date(adds days up until january 1st of argument year)
    for yearInc in range(1900,year):
        if isLeapYear(yearInc):
            dayNum += 366
        else:
            dayNum += 365
            
    #add days from month of date using the month number
    for monthInc in range(0,month):
        if monthInc == 1 and isLeapYear(year):
            dayNum += 29 #Special case for leap day
            
        else:
            dayNum += monthDayCount[monthInc]
        
   
    dayNum += day - 1
    
    
    return dayNum


def dayNumToDayWeek(dayNum):
    dayWeek = dayName[dayNum % 7]
    return dayWeek

def dayNumToDate(dayNumCopy):
    
    #Finding correct year
    
    
    year = 1900 #Initial Year for our Setup
    #Maybe improve
    while dayNumCopy >= 0:
        if isLeapYear(year):
            dayNumCopy -= 366 #Are these correct
        else:
            dayNumCopy -= 365
        year += 1
        
    #At this point, the dayNumCopy is now negative, so we know that we incremented exactly one extra year futher then we are supposed to
    year -= 1
    if isLeapYear(year):
        dayNumCopy += 366
    else:
        dayNumCopy += 365
    #Now we have the correct year, as well as a dayNumCopy which is the number of days from january 1st of that year
    
    
    #Find month and day
    month = 0 #Initial Month
    
    #Exceptions for if it's a leap year, just checks on january and feburary
    if isLeapYear(year):
        if dayNumCopy >= 31: #Check for january
            dayNumCopy -= 31
            month += 1
            if dayNumCopy >= 29: #Check for feburary
                dayNumCopy -= 29
                month += 1
            else:
                day = dayNumCopy + 1
                return month, day, year
        
            
    
    while dayNumCopy >= monthDayCount[month]:
        dayNumCopy -= monthDayCount[month]
        month += 1
    
    day = dayNumCopy + 1
    
    return month, day, year


if __name__ == "__main__":

    
    startDate = dateToDayNum(monthName["January"],1,1901)
    endDate = dateToDayNum(monthName["December"], 31, 2000)
    
    
    sundayCount = 0
    for dayNumInc in range(startDate,endDate+1):
        if dayNumToDayWeek(dayNumInc) == "Sunday":
            date = dayNumToDate(dayNumInc)
            if date[1] == 1:
                sundayCount += 1
                #print("Date: {}- WeekDay: {}- dayNum: {}- Sunday Count: {}".format(date,dayNumToDayWeek(dayNumInc),dayNumInc,sundayCount))
                
                
    print(sundayCount)
    