#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.


def getMinimumCost(k, c):
    n = len(c)
    # 친구들이 꽃의 개수보다 많은 경우 중복으로 사는경우가 없으므로 모두 더한 값을 리턴
    if k >= n:
        return sum(c)
    
    # 중복으로 사는것을 최소화 한다.
    c.sort(reverse=True)
    answer = sum(c[:k])

    remainNum = n - k
    c = c[k:]
    multNum = 2
    count = 0
    for i in range(remainNum):
        answer += multNum*c[i]
        count += 1
        if count == k:
            multNum += 1
            count = 0
    
    return answer




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
