from collections import deque
import math

n, m = map(int, input().split())

mat = []
for _ in range(n):
    row = list(map(int, list(input())))
    mat.append(row)


def bfs(mat):
    q = deque()
    q.append((0, 0, 0))  # 좌표 + 벽을 부셨는지 나타내는 인자
    dist = [[[math.inf]*m for _ in range(n)] for _ in range(2)]
    dist[0][0][0] = dist[1][0][0] = 1

    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while q:
        k, i, j = q.popleft()
        ndist = dist[k][i][j] + 1

        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if mat[ni][nj] == 0 and dist[k][ni][nj] > ndist:
                    dist[k][ni][nj] = ndist
                    q.append((k, ni, nj))
                elif mat[ni][nj] == 1 and dist[1][ni][nj] > ndist and k == 0:
                    dist[1][ni][nj] = ndist
                    q.append((1, ni, nj))
    return dist


dist = bfs(mat)

ans = 0
if dist[0][n-1][m-1] == math.inf and dist[1][n-1][m-1] == math.inf:
    ans = -1
else:
    ans = min(dist[0][n-1][m-1], dist[1][n-1][m-1])

print(ans)
