#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

# Complete the reverseShuffleMerge function below.


def reverseShuffleMerge(s):
    charCounter = Counter(s)  # 전체에서 char의 개수
    usedChar = defaultdict(lambda: 0)  # 현재 a에 사용된 개수
    remainChar = dict(charCounter)  # 아직 조회하지 않은 개수

    # a에 char를 사용할 수 있는지 확인
    def can_use(char):
        if charCounter[char] // 2 - usedChar[char] > 0:
            return True
        return False

    # pop해도 남은 char로 만들 수 있는지 확인
    def can_pop(char):
        if usedChar[char] + remainChar[char] - 1 >= charCounter[char]//2:
            return True
        return False

    a = []
    for char in s[::-1]:
        if can_use(char):
            # 현재 char가 작으면 가능한 가장 앞으로 오게 만든다.
            while a and a[-1] > char and can_pop(a[-1]):
                usedChar[a.pop()] -= 1
            usedChar[char] += 1
            a.append(char)
        remainChar[char] -= 1
    return "".join(a)


if __name__ == '__main__':
    s = input()

    result = reverseShuffleMerge(s)

    print(result)
