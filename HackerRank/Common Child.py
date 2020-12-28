#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.


def commonChild(s1, s2):
    cache = [[0 for _ in range(len(s1)+1)]for _ in range(len(s2)+1)]

    for i2 in range(len(s2)):
        for i1 in range(len(s1)):
            c1 = s1[i1]
            c2 = s2[i2]

            if c1 == c2:
                cache[i2+1][i1+1] = cache[i2][i1] + 1
            else:
                cache[i2+1][i1+1] = max(cache[i2][i1+1], cache[i2+1][i1])
    return cache[-1][-1]


if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(result)
