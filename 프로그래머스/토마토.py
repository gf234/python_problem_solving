import sys
from collections import deque
import math
m, n = map(int, input().split())

mat = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    mat.append(row)

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

dist = [[math.inf]*m for _ in range(n)]


def bfs(mat, dist):
    q = deque()
    ret = -1
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                q.append((i, j))
                dist[i][j] = 0
                ret = 0

    while len(q) != 0:
        x, y = q.popleft()

        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if mat[nx][ny] == 0:
                    ndist = dist[x][y] + 1
                    dist[nx][ny] = ndist
                    mat[nx][ny] = ndist
                    ret = ndist
                    q.append((nx, ny))
    return ret

ans = bfs(mat, dist)
for row in mat:
    b = False
    for x in row:
        if x == 0:
            ans = -1
            b = True
            break
    if b:
        break;

print(ans)
