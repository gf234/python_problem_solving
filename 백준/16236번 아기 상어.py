import math
from collections import deque, defaultdict

n = int(input())

sharkPos = None
sharkSize = 2
eat = 0

adj = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 9:
            sharkPos = (i, j)
            row[j] = 0
    adj.append(row)


def bfs():
    q = deque()
    q.append(sharkPos)

    dist = defaultdict(lambda: math.inf)
    dist[sharkPos] = 0
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    possibles = []
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = dist[(x, y)]+1
            if 0 <= nx < n and 0 <= ny < n and adj[nx][ny] <= sharkSize and dist[(nx, ny)] > nd:
                dist[(nx, ny)] = nd
                q.append((nx, ny))
                if 0 < adj[nx][ny] < sharkSize:
                    possibles.append((nd, (nx, ny)))
    possibles.sort()
    return possibles


time = 0
while True:
    possibles = bfs()

    if possibles:
        temp = possibles[0]
        eat += 1
        time += temp[0]
        if eat == sharkSize:
            eat = 0
            sharkSize += 1
        adj[temp[1][0]][temp[1][1]] = 0
        sharkPos = temp[1]
    else:
        break
print(time)
