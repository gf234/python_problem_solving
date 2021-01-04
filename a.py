#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.


def triplets(a, b, c):
    answer = 0

    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))

    ai = 0
    ci = 0
    for bb in b:
        while ai < len(a) and a[ai] <= bb:
            ai += 1
        while ci < len(c) and c[ci] <= bb:
            ci += 1
        answer += ai * ci
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
