# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 21:31:17 2022

@author: willi
"""
if __name__=="__main__":
    exp = 1000
    numString = str(2**exp)
    sum = 0
    
    for digit in str(numString):
        sum += int(digit)
    print(sum)