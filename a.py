from itertools import combinations
from collections import Counter


def solution(a):
    if len(a) < 2:
        return 0

    c = Counter(a)
    if len(c) >= 2:
        answer = 2
    else:
        return 0
    

    return answer
