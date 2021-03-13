from collections import defaultdict
import sys
import math


def input(): return sys.stdin.readline().rstrip()


n = int(input())
blacks = []
whites = []
mat = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            if (i+j) % 2 == 0:
                blacks.append((i, j))
            else:
                whites.append((i, j))
    mat.append(row)


def check(x, y):
    dxy = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        while 0 <= nx < n and 0 <= ny < n:
            if mat[nx][ny] == 2:
                return False
            nx += dx
            ny += dy
    return True


def backtrack(possibles, ind):
    l = len(possibles)
    if ind == l:
        return 0

    x, y = possibles[ind]
    ret = 0
    if check(x, y):
        mat[x][y] = 2
        ret = 1 + backtrack(possibles, ind+1)
        mat[x][y] = 1
    ret = max(ret, backtrack(possibles, ind+1))
    return ret


answer = backtrack(whites, 0)+backtrack(blacks, 0)
print(answer)
