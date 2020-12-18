#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

# Complete the isValid function below.


def isValid(s):
    cntCounter = Counter(Counter(s).values())
    if len(cntCounter) > 2:
        return 'NO'
    if len(cntCounter) == 1:
        return 'YES'

    a, b = cntCounter.keys()
    if a < b:
        a, b = b, a
    if 1 in cntCounter.values() and (((a-b) == 1 and cntCounter[a] == 1) or (b == 1) and cntCounter[b] == 1):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
