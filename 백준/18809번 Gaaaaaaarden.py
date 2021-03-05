import sys
import math
import copy
from itertools import permutations
from collections import deque


def input(): return sys.stdin.readline().rstrip()


n, m, g, r = map(int, input().split())
mat = []
possibles = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            possibles.append((i, j))
    mat.append(row)


def next(mat, q):
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)

    l = len(q)
    temp = set()
    flowerNum = 0
    for _ in range(l):
        x, y, color = q.popleft()
        opColor = 4 if color == 3 else 3

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1 and (nx, ny, color) not in temp:
                if (nx, ny, opColor) in temp:
                    mat[nx][ny] = 5
                    temp.remove((nx, ny, opColor))
                    flowerNum += 1
                else:
                    temp.add((nx, ny, color))
    for x, y, color in temp:
        mat[x][y] = color
        q.append((x, y, color))
    if not q and flowerNum == 0:
        return -1
    else:
        return flowerNum


def unique_permutations(iterable, r):
    previous = tuple()
    for p in permutations(iterable, r):
        if p > previous:
            previous = p
            yield p


possibleNum = len(possibles)
permutTemp = [1 for _ in range(possibleNum-g-r)] + \
    [3 for _ in range(g)] + [4 for _ in range(r)]
permuts = unique_permutations(permutTemp, possibleNum)
answer = -math.inf
for permut in permuts:
    tempMat = copy.deepcopy(mat)
    flowerNum = 0
    q = deque()
    for i in range(possibleNum):
        x, y = possibles[i]
        tempMat[x][y] = permut[i]
        if permut[i] != 1:
            q.append((x, y, permut[i]))

    while True:
        temp = next(tempMat, q)
        if temp == -1:
            break
        flowerNum += temp
    answer = max(answer, flowerNum)
print(answer)
