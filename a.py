from collections import deque


def solution(gems):
    start = 1
    end = 1
    startGem = -1
    choosed = set()
    for i, gem in enumerate(gems, 1):
        if gem not in choosed:
            end = i
            choosed.add(gem)
