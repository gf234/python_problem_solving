import sys


def read(): return sys.stdin.readline().rstrip()


n, m = map(int, read().split())

board = []
for _ in range(n):
    board.append(list(map(int, read().split())))

# 행마다 합을 저장한다.
for i in range(n):
    for j in range(1, n):
        board[i][j] += board[i][j-1]

for _ in range(m):
    i, j, x, y = map(int, read().split())
    answer = 0
    # board 가 0부터 시작하는것을 생각해준다.
    for k in range(i-1, x):
        if j != 1:
            answer -= board[k][j-2]
        answer += board[k][y-1]
    print(answer)
