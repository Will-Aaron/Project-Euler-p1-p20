# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 20:26:02 2022

@author: willi
"""

#Project Euler Problem 18- Maximum Path Sum 1


def maxSumTree(tree):
    
    #maxSum = 0
    
    for i in range(len(tree)-2,-1,-1):#Iterate Starting at the second to last row
        
        for j in range(len(tree[i])):#Iterate over the ith row to sum the maximum of their children to their parent
            tree[i][j] += max(tree[i+1][j],tree[i+1][j+1])
    return tree[0][0]        

def formatTree(rawString):
    
    tree = rawString.split('\n')
    
    for k in range(len(tree)):
        tree[k] = tree[k].split()
        for n in range(len(tree[k])):
            tree[k][n] = int(tree[k][n])
    return tree


if __name__=="__main__":
    
    print("Please Copy-Paste String")
    rawString = input()
    
    tree = formatTree(rawString)
    
    print(maxSumTree(tree))