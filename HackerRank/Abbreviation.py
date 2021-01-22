#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque, defaultdict

# Complete the abbreviation function below.


def isEqual(a, b):
    return a == b or a.upper() == b


def abbreviation(a, b):
    # dp[i][j]: a[:i]로 b[:j]를 만들 수 있는지
    dp = [[False for _ in range(len(b)+1)]for _ in range(len(a)+1)]
    dp[0][0] = True

    for i in range(1, len(a) + 1):
        for j in range(0, len(b) + 1):
            # 하나씩 지운걸로 만들 수 있고 현재 값으로 만들 수 있으면 True
            if j > 0 and dp[i-1][j-1] and isEqual(a[i-1], b[j-1]):
                dp[i][j] = True
            # 소문자여서 하나 지울 수 있고 지운걸로 만들 수 있으면 True
            if ord(a[i-1]) >= 97 and dp[i-1][j]:
                dp[i][j] = True

    return "YES" if dp[-1][-1] else "NO"


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result)
