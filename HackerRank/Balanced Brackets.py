#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.


def isBalanced(s):
    stack = ['x']
    match = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for c in s:
        if c not in match:
            stack.append(c)
        else:
            if stack[-1] == match[c]:
                stack.pop()
            else:
                return "NO"

    if len(stack) == 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
