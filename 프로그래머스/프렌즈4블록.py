from collections import deque


def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    def check():
        remove = set()
        dij = ((1, 0), (0, 1), (1, 1))
        for i in range(m-1):
            for j in range(n-1):
                c = board[i][j]
                if c == 'X':
                    continue
                for di, dj in dij:
                    ni, nj = i+di, j+dj
                    if board[ni][nj] != c:
                        break
                else:
                    remove.add((i, j))
                    for di, dj in dij:
                        ni, nj = i+di, j+dj
                        remove.add((ni, nj))
        return remove

    def downBlock(remove):
        for i, j in remove:
            board[i][j] = 'X'
        for j in range(n):
            tempCols = deque()
            for i in range(m):
                if board[i][j] != 'X':
                    tempCols.append(board[i][j])
            if tempCols:
                for i in range(m-len(tempCols)):
                    board[i][j] = 'X'
                for i in range(m-len(tempCols), m):
                    board[i][j] = tempCols.popleft()
    ans = 0
    while True:
        remove = check()
        if not remove:
            break
        ans += len(remove)
        downBlock(remove)
    return ans


m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))
