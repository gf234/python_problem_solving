#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.


def largestRectangle(h):
    # 중간부터 시작해서 확장해나간다.
    def findMaxArea(height, s, m, e):
        i, j = m, m+1
        area = 0
        h = min(height[i], height[j])
        while i >= s and j <= e:
            h = min(h, height[i], height[j])
            area = max(area, (j-i+1)*h)
            if i == s:
                j += 1
            elif j == e:
                i -= 1
            else:
                # 높이가 큰 쪽으로 확장
                if height[i-1] > height[j+1]:
                    i -= 1
                else:
                    j += 1
        return area
    # 분할정복을 이용해서 값을 구한다.
    def divide(height, s, e):
        if s == e:
            return height[s]

        m = s + (e-s)//2

        area = divide(height, s, m)

        area = max(area, divide(height, m+1, e))

        area = max(area, findMaxArea(height, s, m, e))
        return area

    return divide(h, 0, len(h)-1)


if __name__ == '__main__':

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    print(result)
