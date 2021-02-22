from collections import Counter
import sys


def read(): return sys.stdin.readline().rstrip()


n, m = map(int, read().split())

board = []
for _ in range(n):
    row = list(map(int, read().split()))
    board.append(row)


def dfs(start):
    stack = [start]

    visited = set()
    visited.add(start)
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    counter = Counter()
    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1:
                    counter[(nx, ny)] += 1
                elif (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append((nx, ny))

    melted = 0
    for key, value in counter.items():
        x, y = key
        if value >= 2:
            board[x][y] = 0
            melted += 1
    return melted


answer = 0
while True:
    melted = dfs((0, 0))
    if melted:
        answer += 1
    else:
        break
print(answer)
