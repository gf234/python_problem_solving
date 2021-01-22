#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.


def stepPerms(n):
    cache = dict()

    def recur(i):
        if i in cache:
            return cache[i]
        if i == n:
            return 1
        if i > n:
            return 0

        ret = recur(i+1)+recur(i+2)+recur(i+3)
        cache[i] = ret
        return ret

    return recur(0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
