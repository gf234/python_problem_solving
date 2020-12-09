import math
from collections import deque


def solution(n, weak, dist):
    dist.sort(reverse=True)
    nw = len(weak)
    nd = len(dist)
    cnt = 0

    prevs = [()]

    for d in dist:
        can_repairs = []
        cnt += 1

        for i, start in enumerate(weak):
            spots = weak[i:] + [n+w for w in weak]
            can = [spot % n for spot in spots if spot - start <= d]
            can_repairs.append(set(can))
        
        possible_set = set()
        for can_repair in can_repairs:
            for prev in prevs:
                new = can_repair | set(prev)
                if len(new) == nw:
                    return cnt
                possible_set.add(tuple(new))
        prevs = possible_set
    return -1


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))
