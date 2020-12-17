#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.


def makeAnagram(a, b):
    da = Counter(a)
    db = Counter(b)
    print(da)
    ans = 0

    del_key = []
    for key in da:
        if key in db:
            ans += abs(da[key]-db[key])
        else:
            ans += da[key]
        del_key.append(key)

    for key in del_key:
        da.pop(key)
        if key in db:
            db.pop(key)

    for key in db:
        ans += db[key]
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
