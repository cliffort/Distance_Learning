#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive_nums=0
    negative_nums=0
    zeros=0
    for i in range(len(arr)):
        if arr[i]>0:
            positive_nums+=1
        elif arr[i]==0:
            zeros+=1
        else:
            negative_nums+=1
    print(positive_nums/len(arr))
    print(negative_nums/len(arr))
    print(zeros/len(arr))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
