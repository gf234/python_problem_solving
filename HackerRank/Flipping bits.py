#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.


def flippingBits(n):
    # int를 unsigned int로 변환하려면 & 0xffffffff를 해주면 된다.
    return int(bin(~n & 0xffffffff), 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
