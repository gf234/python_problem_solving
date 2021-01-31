#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.


def pairs(k, arr):
    numSet = set(arr)

    answerSet = set()
    for num in arr:
        if num+k in numSet:
            answerSet.add(frozenset((num, num+k)))
        if num-k in numSet:
            answerSet.add(frozenset((num, num-k)))
    return len(answerSet)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()