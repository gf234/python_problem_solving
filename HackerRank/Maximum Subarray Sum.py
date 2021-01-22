#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the maximumSum function below.


def maximumSum(a, m):
    answer = 0

    # arrSum의 빼기로 subArr의 합을 구하고 모듈로한 값을 저장한다.
    # ex) a[i:j+1]  -> (sumA[j] - sumA[i-1] + m) % m

    # bst 로 이용할 배열. sumA를 기억한다. 처음 값 계산을 위해 0을 넣어둔다.
    sortedArr = [0]
    # 합을 계산하기 위해 이전 값을 기억한다.
    prev = 0
    for num in a:
        prev = (prev+num) % m
        answer = max(answer, prev)
        # bisect를 이용해 정렬된 상태를 유지하도록 값을 삽입한다.
        bisect.insort(sortedArr, prev)
        # 현재 값보다 큰 값이 이전에 나왔는지 확인.
        # 현재 값보다 큰 값을 뺐을 때 현재 값보다 모듈로 값이 커질 수 있다.
        i = bisect.bisect_right(sortedArr, prev)
        if i < len(sortedArr):
            answer = max(answer, (prev - sortedArr[i] + m) % m)
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
