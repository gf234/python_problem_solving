from collections import deque
import math
n, m = map(int, input().split())

mat = []
for _ in range(n):
    row = list(map(int, list(input())))
    mat.append(row)


def bfs(mat):
    queue = deque()
    queue.append((0, 0))
    dist = [[math.inf] * m for _ in range(n)]
    dist[0][0] = 1

    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while len(queue) != 0:
        i, j = queue.popleft()

        for x, y in dir:
            ni = i+x
            nj = j+y

            if 0 <= ni < n and 0 <= nj < m:
                if mat[ni][nj] == 1:
                    ndist = dist[i][j] + 1
                    if ndist < dist[ni][nj]:
                        queue.append((ni, nj))
                        dist[ni][nj] = ndist

    return dist


dist = bfs(mat)

print(dist[n-1][m-1])
