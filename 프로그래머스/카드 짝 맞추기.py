import math
from itertools import permutations
from collections import defaultdict, deque


def solution(board, r, c):
    global answer
    answer = math.inf
    # 쉬프트 누르고 이동하는 경우 좌표들을 반환

    def shift(start):
        ret = []
        x, y = start
        dx = (1, 0, -1, 0)
        dy = (0, 1, 0, -1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True:
                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                    nx -= dx[i]
                    ny -= dy[i]
                    ret.append((nx, ny))
                    break
                if board[nx][ny] != 0:
                    ret.append((nx, ny))
                    break
                nx += dx[i]
                ny += dy[i]
        return ret
    # 특정 지점간 최소 거리 반환

    def dist(start, target):
        if start == target:
            return 0
        q = deque()
        q.append(start)
        dist = defaultdict(lambda: math.inf)
        dist[start] = 0
        dx = (1, 0, -1, 0)
        dy = (0, 1, 0, -1)
        while q:
            x, y = q.popleft()
            nd = dist[(x, y)] + 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 4 and 0 <= ny < 4 and dist[(nx, ny)] > nd:
                    if (nx, ny) == target:
                        return nd
                    dist[(nx, ny)] = nd
                    q.append((nx, ny))

            shifts = shift((x, y))
            for nx, ny in shifts:
                if 0 <= nx < 4 and 0 <= ny < 4 and dist[(nx, ny)] > nd:
                    if (nx, ny) == target:
                        return nd
                    dist[(nx, ny)] = nd
                    q.append((nx, ny))
    # 뒤집어야 하는 카드들의 좌표를 저장
    cards = defaultdict(list)
    # 뒤집어야 하는 카드의 번호를 저장
    temp = set()
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards[board[i][j]].append((i, j))
                temp.add(board[i][j])
    # 뒤집는 순서 모든 경우
    permuts = permutations(sorted(temp))
    for permut in permuts:
        l = len(permut)
        # 특정 번호의 카드를 뒤집는 순서도 고려해준다.

        def recur(board, pos, ind, sum):
            global answer
            if sum >= answer:
                return
            if ind == l:
                if answer > sum:
                    answer = sum
                return

            temp = cards[permut[ind]]
            ret1 = dist(pos, temp[0]) + dist(temp[0], temp[1])
            for x, y in temp:
                board[x][y] = 0
            recur(board, temp[1], ind + 1, sum+ret1+2)
            for x, y in temp:
                board[x][y] = permut[ind]

            ret2 = dist(pos, temp[1]) + dist(temp[1], temp[0])
            for x, y in temp:
                board[x][y] = 0
            recur(board, temp[0], ind + 1, sum+ret2+2)
            for x, y in temp:
                board[x][y] = permut[ind]
        recur(board, (r, c), 0, 0)
    return answer


board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
r = 0
c = 1
print(solution(board, r, c))
