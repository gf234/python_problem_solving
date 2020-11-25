import sys
from collections import deque

N, L, R = map(int, input().split())

A = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    A.append(row)

# 1. 인접하는 나라가 열리는지 확인하고 표시
# 2. 열려있는 나라들을 합치고 인구수 수정
# 반복

cnt = 0

while True:
    visited = [[False] * N for _ in range(N)]

    def bfs(i, j):
        q = deque()
        q.append((i, j))
        visited[i][j] = True

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ret = [(i, j)]

        while q:
            x, y = q.popleft()

            for dx, dy in dir:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny]:
                        if L <= abs(A[nx][ny]-A[x][y]) <= R:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            ret.append((nx, ny))
        return ret

    is_move = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = bfs(i, j)
                if len(union) > 1:
                    is_move = True
                    sum = 0
                    for x, y in union:
                        sum += A[x][y]
                    sum = sum//len(union)

                    for x, y in union:
                        A[x][y] = sum

    if is_move:
        cnt += 1
    else:
        break

print(cnt)
