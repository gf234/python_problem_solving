import sys
import math
from collections import deque


def input(): return sys.stdin.readline().rstrip()


n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

islands = []
visited = [[False for _ in range(n)] for _ in range(n)]


def dfs(i, j):
    stack = []
    stack.append((i, j))
    visited[i][j] = True
    dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))
    island = set()
    island.add((i, j))
    while stack:
        x, y = stack.pop()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and mat[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))
                island.add((nx, ny))
    return island


for i in range(n):
    for j in range(n):
        if mat[i][j] == 1 and not visited[i][j]:
            island = dfs(i, j)
            islands.append(island)


answer = math.inf


def bfs(island):
    q = deque()
    dist = [[math.inf for _ in range(n)] for _ in range(n)]
    for i, j in island:
        q.append((i, j))
        dist[i][j] = 0
    dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))
    while q:
        x, y = q.popleft()
        if dist[x][y] == answer:
            return answer

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 > nx or 0 > ny or nx >= n or ny >= n:
                continue
            nd = dist[x][y] + 1
            if mat[nx][ny] == 0 and dist[nx][ny] > nd:
                dist[nx][ny] = nd
                q.append((nx, ny))
            if nd != 1 and mat[nx][ny] == 1 and (nx, ny) not in island:
                return nd-1


for island in islands:
    answer = bfs(island)
print(answer)
