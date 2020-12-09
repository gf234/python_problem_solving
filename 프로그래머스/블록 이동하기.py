from collections import deque, defaultdict
import math


def solution(board):
    answer = 0
    n = len(board)
    board = [[1]+row+[1] for row in board]
    board = [[1 for _ in range(n+2)]] + board + [[1 for _ in range(n+2)]]
    start = ((1, 1), (1, 2))
    q = deque()
    q.append(start)
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    while q:
        a, b = q.popleft()
        ndist = dist[(a, b)] + 1
        # 가능한 점 찾아서 큐에 추가
        # 가로인 경우
        if a[0] == b[0]:
            if board[a[0]+1][a[1]] == 0 and board[a[0]+1][a[1]+1] == 0:
                there = (b, (a[0]+1, a[1]+1))
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
                there = (a, (a[0]+1, a[1]))
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
                there = ((a[0]+1, a[1]), (a[0]+1, a[1]+1))
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
            if board[a[0]-1][a[1]] == 0 and board[a[0]-1][a[1]+1] == 0:
                there = ((a[0]-1, a[1]), a)
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
                there = ((a[0]-1, a[1]+1), b)
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
                there = ((a[0]-1, a[1]), (a[0]-1, a[1]+1))
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
            if board[b[0]][b[1]+1] == 0:
                there = (b, (b[0], b[1]+1))
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
            if board[a[0]][a[1]-1] == 0:
                there = ((a[0], a[1]-1), a)
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
        # 세로인 경우
        else:
            if board[a[0]][a[1]-1] == 0 and board[b[0]][b[1]-1] == 0:
                there = ((a[0], a[1]-1), a)
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
                there = ((b[0], b[1]-1), b)
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
                there = ((a[0], a[1]-1), (b[0], b[1]-1))
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
            if board[a[0]][a[1]+1] == 0 and board[b[0]][b[1]+1] == 0:
                there = (a, (a[0], a[1]+1))
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
                there = (b, (b[0], b[1]+1))
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
                there = ((a[0], a[1]+1), (b[0], b[1]+1))
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
            if board[a[0]-1][a[1]] == 0:
                there = ((a[0]-1, a[1]), a)
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
            if board[b[0]+1][b[1]] == 0:
                there = (b, (b[0]+1, b[1]))
                if dist[there] > ndist:
                    dist[there] = ndist
                    q.append(there)
    answer = min(dist[((n-1, n), (n, n))], dist[((n, n-1), (n, n))])
    return answer


board = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [
    0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]

print(solution(board))
