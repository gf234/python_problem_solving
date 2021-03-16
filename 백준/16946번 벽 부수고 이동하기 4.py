import sys


def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
mat = []
for _ in range(n):
    row = list(map(int, list(input())))
    mat.append(row)


visited = [[False for _ in range(m)]for _ in range(n)]


def dfs(i, j):
    cnt = 1
    stack = [(i, j)]
    visited[i][j] = True
    dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))
    temp = set()
    while stack:
        x, y = stack.pop()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if mat[nx][ny] == 0 and not visited[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                elif mat[nx][ny] != 0:
                    temp.add((nx, ny))

    for x, y in temp:
        mat[x][y] = mat[x][y]+cnt


for i in range(n):
    for j in range(m):
        if mat[i][j] == 0 and not visited[i][j]:
            dfs(i, j)

for i in range(n):
    for j in range(m):
        print(mat[i][j] % 10, end='')
    print()
