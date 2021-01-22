#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque

# Complete the roadsAndLibraries function below.


def roadsAndLibraries(n, c_lib, c_road, cities):
    adj = [[] for _ in range(n)]
    for a, b in cities:
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)

    if c_lib <= c_road:
        return c_lib*n

    visited = set()

    def bfs(start):
        numNode = 0
        q = deque()
        q.append(start)
        visited.add(start)
        while q:
            here = q.popleft()
            numNode += 1
            for there in adj[here]:
                if there not in visited:
                    visited.add(there)
                    q.append(there)
        return numNode

    answer = 0
    for i in range(n):
        if i not in visited:
            numNode = bfs(i)
            answer += c_lib + c_road*(numNode-1)
    return answer


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(result)
