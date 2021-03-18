import sys


def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)


def melt():
    dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))
    ret = None
    icenum = 0
    temp = []
    for x in range(n):
        for y in range(m):
            if mat[x][y] != 0:
                cnt = 0
                for dx, dy in dxy:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 0:
                        cnt += 1
                height = mat[x][y] - cnt
                if height <= 0:
                    temp.append((x, y, 0))
                else:
                    temp.append((x, y, height))
                    ret = (x, y)
                    icenum += 1
    for x, y, height in temp:
        mat[x][y] = height
    return ret, icenum


def dfs(i, j):
    stack = [(i, j)]
    visited = [[False for _ in range(m)]for _ in range(n)]
    visited[i][j] = True
    dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))
    cnt = 0
    while stack:
        x, y = stack.pop()
        cnt += 1

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))
    return cnt


def solve():
    time = 0
    while True:
        time += 1
        start, cnt = melt()
        if cnt == 0:
            return 0
        i, j = start
        if dfs(i, j) != cnt:
            return time


print(solve())
