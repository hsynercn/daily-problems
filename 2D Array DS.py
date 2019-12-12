#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(x):
    max = -82
    for i in range(len(x)-2):
        for j in range(len(x[i])-2):
            sum = x[i][j]+x[i][j+1]+x[i][j+2]+x[i+1][j+1]+x[i+2][j]+x[i+2][j+1]+x[i+2][j+2]
            if sum>max:
                max = sum
    return max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()