import math
from collections import deque


def solution(board):
    n = len(board)
    q = deque()
    q.append((0, 0, 0, -1))
    dist = [[math.inf for _ in range(n)]for _ in range(n)]
    dist[0][0] = 0
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while q:
        hd, hx, hy, hdir = q.popleft()

        for i in range(4):
            if hdir == -1:
                nd = 100
            elif i == ((hdir+2) % 4):
                continue
            elif i == hdir:
                nd = hd+100
            else:
                nd = hd+600
            dx, dy = dir[i]
            nx = hx + dx
            ny = hy + dy

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0 and dist[nx][ny] >= nd:
                    dist[nx][ny] = nd
                    q.append((nd, nx, ny, i))
    return dist[-1][-1]
