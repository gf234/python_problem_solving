#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque, defaultdict

# Complete the minimumMoves function below.


def minimumMoves(grid, startX, startY, goalX, goalY):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append((startX, startY))
    dist = defaultdict(lambda: math.inf)
    dist[(startX, startY)] = 0
    answer = math.inf
    n = len(grid)
    while q:
        x, y = q.popleft()
        d = dist[(x, y)]

        for dir in range(4):
            nx, ny = x, y
            while True:
                nx, ny = nx + dx[dir], ny+dy[dir]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '.':
                    if (nx, ny) == (goalX, goalY):
                        return d + 1
                    elif dist[(nx, ny)] > (d+1):
                        dist[(nx, ny)] = d + 1
                        q.append((nx, ny))
                else:
                    break


if __name__ == '__main__':
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print(result)
