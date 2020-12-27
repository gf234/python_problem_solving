#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the countInversions function below.


def countInversions(arr):

    def merge_sort(arr):
        n = len(arr)
        if n == 1:
            return arr, 0

        mid = n//2
        arrOne, oneSwapCount = merge_sort(arr[:mid])
        arrTwo, twoSwapCount = merge_sort(arr[mid:])

        ret, retSwapCount = merge(arrOne, arrTwo)
        swapCount = oneSwapCount+twoSwapCount+retSwapCount
        return ret, swapCount

    def merge(a, b):
        ret = []
        # 앞에서 꺼내는 것을 빨리 하기 위해 deque 사용
        a = deque(a)
        b = deque(b)
        inversions = 0

        while a and b:
            # 뒤집힌 개수를 센다.
            if a[0] > b[0]:
                ret.append(b.popleft())
                inversions += len(a)
            else:
                ret.append(a.popleft())

        while a:
            ret.append(a.popleft())

        while b:
            ret.append(b.popleft())

        return ret, inversions

    sortedArr, answer = merge_sort(arr)
    print(sortedArr)
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
