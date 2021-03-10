import sys
from collections import deque


def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
mat = []
for _ in range(n):
    row = list(map(int, list(input())))
    mat.append(row)


def bfs(x, y, height):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    count = 1
    possible = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 가장자리는 수영장이 될 수 없다.
            if nx < 0 or ny < 0 or nx == n or ny == m:
                possible = False
                continue
            # height 보다 낮은 영역을 구해서 더해준다.
            if mat[nx][ny] < height and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1
    if possible:
        return count
    else:
        return 0


answer = 0
for height in range(2, 10):
    visited = [[False for _ in range(m)]for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if not visited[i][j] and mat[i][j] < height:
                answer += bfs(i, j, height)
print(answer)
