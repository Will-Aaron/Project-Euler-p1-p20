# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:01:23 2021

@author: willi
"""
def modIt(n):
    n = n%10000000000
    return n

if __name__ == "__main__":
    print("place in numbers")
    s = input()
    listA = s.split('\n')
    listA = list(map(int,listA))
    print('size '+str(len(listA)))
    print('All numbers')
    print(listA)
    #listA = list(map(modIt,listA))
    total = sum(listA)
    Final = str(total)[:10]
    print('Final: '+str(Final))
    