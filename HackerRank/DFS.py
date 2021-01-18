#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxRegion function below.


def maxRegion(grid):
    n = len(grid)
    m = len(grid[0])

    dxy = ((1, 0), (0, 1), (-1, 0), (0, -1),
           (1, 1), (1, -1), (-1, 1), (-1, -1))

    def is_in_grid(x, y):
        if 0 <= x < n and 0 <= y < m:
            return True
        return False
    visited = set()

    def dfs(x, y):
        visited.add((x, y))
        ret = 1

        for dir in range(8):
            nx, ny = x+dxy[dir][0], y+dxy[dir][1]
            if is_in_grid(nx, ny) and grid[nx][ny] == 1 and (nx, ny) not in visited:
                ret += dfs(nx, ny)
        return ret

    answer = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and (i, j) not in visited:
                answer = max(answer, dfs(i, j))
    return answer


if __name__ == '__main__':
    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    print(res)
