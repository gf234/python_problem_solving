#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.


def minimumAbsoluteDifference(arr):
    arr.sort()

    answer = math.inf
    for i in range(len(arr)-1):
        answer = min(answer, abs(arr[i]-arr[i+1]))
    
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
