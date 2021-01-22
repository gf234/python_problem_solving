#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the whatFlavors function below.


def whatFlavors(cost, money):
    costInd = defaultdict(list)

    for i, c in enumerate(cost, 1):
        costInd[c].append(i)

    for cost1 in cost:
        cost2 = money-cost1
        if cost2 in costInd:
            if cost1 == cost2 and len(costInd[cost1]) >= 2:
                indArr = costInd[cost1]
                print(indArr[0], indArr[1])
                return
            if cost1 != cost2:
                print(costInd[cost1][0], costInd[cost2][0])
                return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
