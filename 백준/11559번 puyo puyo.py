import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


mat = []
for _ in range(12):
    row = list(input())
    mat.append(row)


def down():
    for j in range(6):
        column = deque()
        for i in range(12):
            if mat[i][j] != '.':
                column.append(mat[i][j])
        l = len(column)
        for i in range(12-l):
            mat[i][j] = '.'
        for i in range(12-l, 12):
            mat[i][j] = column.popleft()


def dfs(i, j, visited):
    color = mat[i][j]
    stack = [(i, j)]
    visited.add((i, j))
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    count = 0
    temp = []
    while stack:
        x, y = stack.pop()
        temp.append((x, y))
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and (nx, ny) not in visited and mat[nx][ny] == color:
                visited.add((nx, ny))
                stack.append((nx, ny))
    if count >= 4:
        return temp
    return []


answer = 0
while True:
    visited = set()
    explode = []
    for i in range(12):
        for j in range(6):
            if mat[i][j] != '.' and (i, j) not in visited:
                temp = dfs(i, j, visited)
                explode.extend(temp)
    if explode:
        answer += 1
        for x, y in explode:
            mat[x][y] = '.'
        down()
    else:
        break
print(answer)
