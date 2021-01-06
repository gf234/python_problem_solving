#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.


def candies(n, arr):
    # 먼저 1개씩 나눠준다.
    candies = [1 for _ in range(n)]

    # 왼쪽에서 오른쪽으로 가면서 다음 사람이 더 크면 한개를 더 준다.
    for i in range(n-1):
        if arr[i] < arr[i+1]:
            candies[i+1] = candies[i]+1
    # 반대로 오른쪽에서 왼쪽으로 오면서 다음 사람이 더 크고 받은 캔디가 더 적으면 한개를 더 준다.
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1] and candies[i-1] <= candies[i]:
            candies[i-1] = candies[i]+1

    return sum(candies)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
