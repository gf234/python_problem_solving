#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
# Complete the activityNotifications function below.


def countingSort(arr, max):
    count = [0 for _ in range(max+1)]

    for x in arr:
        count[x] += 1
    
    for i in range(1, max+1):
        count[i] += count[i-1]
    
    sortedArr = [0 for _ in range(len(arr))]
    for x in arr:
        sortedArr[count[x]-1] = x
        count[x] -= 1
    return sortedArr

arr = [5,1,6,4,11,7,8,7]
sortedArr=countingSort(arr,11)

print(sortedArr)