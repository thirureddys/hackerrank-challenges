#!/bin/python

import math
import os
import random
import re
import sys

# Complete the findLonely function below.
def findLonely(arr):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    res = findLonely(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
