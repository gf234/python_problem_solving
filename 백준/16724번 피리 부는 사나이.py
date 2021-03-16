import sys


def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
mat = []
for _ in range(n):
    row = list(input())
    mat.append(row)


def dxy(x, y):
    dir = mat[x][y]

    if dir == 'L':
        return 0, -1
    elif dir == 'R':
        return 0, 1
    elif dir == 'U':
        return -1, 0
    else:
        return 1, 0


visited = [[False for _ in range(m)]for _ in range(n)]


def dfs(i, j):
    stack = [(i, j)]
    visited[i][j] = True
    temp = set()
    temp.add((i, j))
    while stack:
        x, y = stack.pop()

        dx, dy = dxy(x, y)
        nx = x + dx
        ny = y + dy

        if not visited[nx][ny]:
            visited[nx][ny] = True
            stack.append((nx, ny))
            temp.add((nx, ny))
        elif (nx, ny) in temp:
            return 1
    return 0


answer = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            answer += dfs(i, j)
print(answer)
