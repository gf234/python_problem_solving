#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the riddle function below.


def riddle(arr):
    # complete this function
    n = len(arr)

    maxWindowSize = dict()
    stack = [0]

    # 각 값마다 최대 윈도우 사이즈를 구한다.
    for i in range(1, n):
        if arr[stack[-1]] <= arr[i]:
            stack.append(i)
        else:
            while arr[stack[-1]] > arr[i]:
                top = arr[stack.pop()]

                if stack:
                    maxWindowSize[top] = i - stack[-1] - 1
                else:
                    maxWindowSize[top] = i
                    break
            stack.append(i)
    else:
        i = n
        while stack:
            top = arr[stack.pop()]

            if stack:
                maxWindowSize[top] = i - stack[-1] - 1
            else:
                maxWindowSize[top] = i

    # 딕셔너리를 뒤집어서 윈도우 사이즈의 최대값을 구한다.
    maxValue = dict()

    for key, value in maxWindowSize.items():
        if value not in maxValue:
            maxValue[value] = key
        else:
            maxValue[value] = max(maxValue[value], key)
    # n부터 1까지 거꾸로 가면서 해당 윈도우 사이즈의 최대 값을 구해서 넣어준다.
    answer = []
    temp = -1
    for i in range(n, 0, -1):
        if i in maxValue:
            temp = max(temp, maxValue[i])
        answer.append(temp)
    # n부터 1까지 구했기 때문에 반전시켜서 리턴
    return reversed(answer)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    print(' '.join(map(str, res)))
