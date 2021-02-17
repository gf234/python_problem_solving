import sys

n = int(input())
adj = []
for _ in range(n):
    row = list(sys.stdin.readline().rstrip())
    adj.append(row)


def dfs(start, visited):
    color = adj[start[0]][start[1]]
    stack = []
    stack.append(start)
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    while stack:
        x, y = stack.pop()
        visited.add((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and adj[nx][ny] == color:
                stack.append((nx, ny))


visited = set()
normal = 0
for i in range(n):
    for j in range(n):
        if (i, j) not in visited:
            normal += 1
            dfs((i, j), visited)
print(normal, end=' ')


def dfs2(start, visited):
    color = adj[start[0]][start[1]]
    stack = []
    stack.append(start)
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    while stack:
        x, y = stack.pop()
        visited.add((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and check(color, nx, ny):
                stack.append((nx, ny))


def check(color, x, y):
    if color == adj[x][y]:
        return True
    if color in {'R', 'G'} and adj[x][y] in {'R', 'G'}:
        return True
    return False


visited = set()
colorBlindness = 0
for i in range(n):
    for j in range(n):
        if (i, j) not in visited:
            colorBlindness += 1
            dfs2((i, j), visited)
print(colorBlindness)
