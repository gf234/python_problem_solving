import sys
from collections import deque
import math
m, n, h = map(int, input().split())

boxs = []
for _ in range(h):
    box = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().rstrip().split()))
        box.append(row)
    boxs.append(box)

dir = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1]]

dist = [[[0]*m for _ in range(n)] for _ in range(h)]


def bfs(boxs, dist):
    q = deque()
    ret = -1
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if boxs[k][i][j] == 1:
                    q.append((k, i, j))
                    dist[k][i][j] = 0
                    ret = 0

    while len(q) != 0:
        k, x, y = q.popleft()

        for dk, dx, dy in dir:
            nk = k + dk
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and 0 <= nk < h:
                if boxs[nk][nx][ny] == 0:
                    ndist = dist[k][x][y] + 1
                    dist[nk][nx][ny] = ndist
                    boxs[nk][nx][ny] = ndist
                    ret = ndist
                    q.append((nk, nx, ny))
    return ret


ans = bfs(boxs, dist)
for box in boxs:
    b2 = False
    for row in box:
        b = False
        for x in row:
            if x == 0:
                ans = -1
                b = True
                break
        if b:
            b2 = True
            break
    if b2:
        break

print(ans)
