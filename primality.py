#!/bin/python

import math
import os
import random
import re
import sys

# Complete the primality function below.
def primality(n):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(raw_input())

    for p_itr in xrange(p):
        n = int(raw_input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
