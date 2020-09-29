# -*- coding: utf-8 -*-

import time

def sumOfN(n):
    start = time.time()
    
    theSum = 0
    
    for i in range(1,n+1):
        theSum = theSum + i
        
    end = time.time()
    
    return theSum, end - start


def sumOfN2(n):
    start = time.time()
    end = time.time()
    return (n*(n+1)/2), end-start


for i in range(5):
    print("Sum  is %d required %10.7f seconds"%sumOfN(100000000))


for i in range(5):
    print("Sum  is %d required %10.7f seconds"%sumOfN2(100000000))