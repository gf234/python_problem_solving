#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.


def luckBalance(k, contests):
    contests.sort(key=lambda x: x[0], reverse=True)
    print(contests)
    answer = 0
    for l, t in contests:
        if t == 0:
            answer += l
        elif k > 0:
            k -= 1
            answer += l
        else:
            answer -= l

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
