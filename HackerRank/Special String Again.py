#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.


def substrCount(n, s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    answer = 0

    for i in range(n):
        substr = s[i]
        char = substr
        answer += 1

        for j in range(i+1, n):
            if s[j] == char:
                answer += 1
                substr += char
            else:
                sameCount = j-i
                rightSubStr = s[j+1:j+1+sameCount]
                if rightSubStr == substr:
                    answer += 1
                break

    return answer


if __name__ == '__main__':
    n = int(input())

    s = input()

    result = substrCount(n, s)

    print(result)
