import sys
from collections import Counter


def input(): return sys.stdin.readline().rstrip()


R, C, K = map(int, input().split())
mat = []
for _ in range(3):
    row = list(map(int, input().split()))
    mat.append(row)


def r():
    r, c = len(mat), len(mat[0])
    maxl = c
    for i in range(r):
        counter = Counter()
        for j in range(c):
            if mat[i][j] != 0:
                counter[mat[i][j]] += 1
        temp = []
        for key, val in counter.items():
            temp.append((val, key))
        temp.sort()
        row = []
        for val, key in temp:
            row.append(key)
            row.append(val)
        maxl = max(maxl, len(row))
        mat[i] = row[:100]
    maxl = min(maxl, 100)
    for i in range(r):
        l = len(mat[i])
        if maxl > l:
            mat[i] += [0 for _ in range(maxl-l)]


def c():
    c = len(mat[0])
    for j in range(c):
        r = len(mat)
        counter = Counter()
        for i in range(r):
            if mat[i][j] != 0:
                counter[mat[i][j]] += 1
        temp = []
        for key, val in counter.items():
            temp.append((val, key))
        temp.sort()
        col = []
        for val, key in temp:
            col.append(key)
            col.append(val)
        l = len(col)
        if r < l:
            for i in range(r):
                mat[i][j] = col[i]
            for i in range(r, min(l, 100)):
                row = [0 for _ in range(j)] + [col[i]] + \
                    [0 for _ in range(c-j-1)]
                mat.append(row)
        else:
            for i in range(l):
                mat[i][j] = col[i]
            for i in range(l, r):
                mat[i][j] = 0


def solve(R, C, K):
    time = 0
    while True:
        row, col = len(mat), len(mat[0])
        if row >= R and col >= C and mat[R-1][C-1] == K:
            break
        time += 1
        if time > 100:
            break
        if row >= col:
            r()
        else:
            c()

    if time == 101:
        return -1
    else:
        return time


print(solve(R, C, K))
