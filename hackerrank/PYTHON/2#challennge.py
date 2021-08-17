 '''
# Task
    Given an integer,N, perform the following conditional actions:
    If N is odd, print Weird
    If N is even and in the inclusive range of 2 to 5, print Not Weird
    If N is even and in the inclusive range of 6 to 20, print Weird
    If N is even and greater than 20, print Not Weird
'''
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if (N % 2) != 0:
        print("Weird")
    elif  (N % 2) == 0 & 2<N<=5 : 
         print("Not Weird")
    elif  (N % 2) == 0 & 6<N<=20 : 
         print("Weird")
    elif  (N % 2) == 0 & 20<N : 
         print("Not Weird")