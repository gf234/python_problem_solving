#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the minTime function below.


def minTime(machines, goal):
    left = 1
    right = min(machines)*goal

    while left <= right:
        mid = (left+right)//2
        produced = 0
        for m in machines:
            produced += mid // m

        if produced >= goal:
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    print(ans)
    # fptr.write(str(ans) + '\n')
