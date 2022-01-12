# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:16:58 2022

@author: willi
"""

import math

if __name__=="__main__":
    digit = map(int, list(str(math.factorial(100))))
    print(sum(digit))